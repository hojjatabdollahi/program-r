"""Majordomo Protocol Worker API, Python version

Implements the MDP/Worker spec at http:#rfc.zeromq.org/spec:7.

Author: Min RK <benjaminrk@gmail.com>
Based on Java example by Arkadiusz Orzechowski
"""

import logging
import time
import zmq

from programy.clients.events.majordomo.config import MajorDomoConfiguration
from programy.majordomo.request import ReadyRequest, UserRequest, SessionRequest, QuestionRequest, ServiceRequest
from programy.majordomo.zhelpers import dump
# MajorDomo protocol constants:
from programy.majordomo import MDP


class MajorDomoWorker(object):
    """Majordomo Protocol Worker API, Python version

    Implements the MDP/Worker spec at http:#rfc.zeromq.org/spec:7.
    """

    HEARTBEAT_LIVENESS = 3  # 3-5 is reasonable
    broker = None
    ctx = None
    service = None

    worker = None  # Socket to broker
    heartbeat_at = 0  # When to send HEARTBEAT (relative to time.time(), so in seconds)
    liveness = 0  # How many attempts left
    heartbeat = 2500  # Heartbeat delay, msecs
    reconnect = 2500  # Reconnect delay, msecs

    # Internal state
    expect_reply = False  # False only at start

    timeout = 2500  # poller timeout
    verbose = False  # Print activity to stdout

    # Return address, if any
    reply_to = None

    def __init__(self, majordomo_config: MajorDomoConfiguration):
        self.ip = majordomo_config.ip
        self.port = majordomo_config.port
        self.service = majordomo_config.service_name
        self.verbose = majordomo_config.verbose
        self.broker = str(self.ip)+":"+str(self.port)

        self.ctx = zmq.Context()
        self.poller = zmq.Poller()
        logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S",
                            level=logging.INFO)
        self.reconnect_to_broker()

    def reconnect_to_broker(self):
        """Connect or reconnect to broker"""
        if self.worker:
            self.poller.unregister(self.worker)
            self.worker.close()
        self.worker = self.ctx.socket(zmq.DEALER)
        self.worker.linger = 0
        self.worker.connect(self.broker)
        self.poller.register(self.worker, zmq.POLLIN)
        if self.verbose:
            logging.info("I: connecting to broker at %s...", self.broker)

        # Register service with broker
        self.send_to_broker(MDP.W_READY, self.service, [])

        # If liveness hits zero, queue is considered disconnected
        self.liveness = self.HEARTBEAT_LIVENESS
        self.heartbeat_at = time.time() + 1e-3 * self.heartbeat

    def send_to_broker(self, command, option=None, msg=None):
        """Send message to broker.

        If no msg is provided, creates one internally
        """
        if msg is None:
            msg = []
        elif not isinstance(msg, list):
            msg = [msg]

        if option:
            msg = [option] + msg

        msg = ['', MDP.W_WORKER, command] + msg
        if self.verbose:
            logging.info("I: sending %s to broker", command)
            dump(msg)

        def enc(item):
            try:
                return item.encode('ascii')
            except:
                #print("Problem cencoding " + str(item) + " to ascii")
                return item

        msg2 = [enc(x) for x in msg]

        self.worker.send_multipart(msg2)

    def _recv(self, reply=None):
        """Send reply, if any, to broker and wait for next request."""
        # Format and send the reply if we were provided one
        assert reply is not None or not self.expect_reply

        if reply is not None:
            assert self.reply_to is not None
            reply = [self.reply_to, ''] + reply
            self.send_to_broker(MDP.W_REPLY, msg=reply)

        self.expect_reply = True

        while True:
            # Poll socket for a reply, with timeout
            try:
                items = self.poller.poll(self.timeout)
            except KeyboardInterrupt:
                break  # Interrupted

            if items:
                msg = self.worker.recv_multipart()
                if self.verbose:
                    logging.info("I: received message from broker: ")
                    dump(msg)

                def dec(item):
                    try:
                        return item.decode('utf-8')
                    except:
                        #print("couldn't decode this: " + str(item))
                        return item

                msg = [dec(x) for x in msg]

                self.liveness = self.HEARTBEAT_LIVENESS
                # Don't try to handle errors, just assert noisily
                assert len(msg) >= 3

                empty = msg.pop(0)
                assert empty == ''

                header = msg.pop(0)
                assert header == MDP.W_WORKER

                command = msg.pop(0)

                try:
                    command = command.encode()
                except:
                    pass

                if command == MDP.W_REQUEST:
                    # We should pop and save as many addresses as there are
                    # up to a null part, but for now, just save one...
                    self.reply_to = msg.pop(0)
                    # pop empty
                    empty = msg.pop(0)
                    assert empty == ''

                    return msg  # We have a request to process
                elif command == MDP.W_HEARTBEAT:
                    # Do nothing for heartbeats
                    pass
                elif command == MDP.W_DISCONNECT:
                    self.reconnect_to_broker()
                else:
                    logging.error("E: invalid input message: ")
                    dump(msg)

            else:
                self.liveness -= 1
                if self.liveness == 0:
                    if self.verbose:
                        logging.warn("W: disconnected from broker - retrying...")
                    try:
                        time.sleep(1e-3 * self.reconnect)
                    except KeyboardInterrupt:
                        break
                    self.reconnect_to_broker()

            # Send HEARTBEAT if it's time
            if time.time() > self.heartbeat_at:
                self.send_to_broker(MDP.W_HEARTBEAT)
                self.heartbeat_at = time.time() + 1e-3 * self.heartbeat

        logging.warn("W: interrupt received, killing worker...")
        return None

    def destroy(self):
        # context.destroy depends on pyzmq >= 2.1.10
        self.ctx.destroy(0)


    def receive(self, reply=None):
        request = self._recv(reply)
        request_object = self.convert_to_request_object(request)
        return request_object


    def convert_to_request_object(self, request):
        if len(request)==1:
            if request[0]=="ready":
                ready_request = ReadyRequest("ready")
                return ready_request

        if len(request)==3:
            if request[0]=="user":
                username = request[2]
                user_request = UserRequest("user", username)
                return user_request

        if len(request)==2:
            if request[0]=="session":
                session_number = request[1]
                session_request = SessionRequest("session", session_number)
                return session_request

            if request[0]=="question":
                question = request[1]
                question_request = QuestionRequest("question", question)
                return question_request

            if request[0]=="service":
                service_name = request[1]
                service_request = ServiceRequest("service", service_name)
                return service_request

        return None