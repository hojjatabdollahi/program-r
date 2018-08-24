import threading
import subprocess
import time
import socket
from programy.utils.logging.ylogger import YLogger


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread
    return wrapper


class StanfordCoreNLPServer():


    def __init__(self, corenlp_dir, port):
        self.corenlp_dir = corenlp_dir
        self.port = port


    @threaded
    def _run_server(self):
        command = 'java -mx1g -cp "'+self.corenlp_dir+'"  edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port ' + str(self.port) +' -timeout 10000'
        p = subprocess.Popen(
            command,
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


    def run(self):
        if self._is_port_open(9000):
            thread = self._run_server()
            time.sleep(1)
            YLogger.debug(self, "run a new server on port 9000")
        else:
            YLogger.debug(self, "Using the current running server")



    def _is_port_open(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = False
        try:
            sock.bind(("0.0.0.0", port))
            result = True
        except Exception as exception:
            YLogger.exception(self, "port is in use for corenlp", exception)
        sock.close()
        return result





