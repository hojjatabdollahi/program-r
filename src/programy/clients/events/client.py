from programy.utils.logging.ylogger import YLogger
from programy.clients.client import BotClient

import os
from datetime import datetime
import yaml
from programy.services.service import ServiceFactory

class EventBotClient(BotClient):

    def __init__(self, id, argument_parser=None):
        self._running = False
        self._first_time = True
        self._session_saving_mode = False
        BotClient.__init__(self, id, argument_parser=argument_parser)

    def prior_to_run_loop(self):
        pass

    def run_loop(self):
        #todo change this back to work with console
        #client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
        self._running = True
        conversation_file = "/home/rohola/conv_questions.p"

        bot = self.bot_factory.bot("bot")

        # mitsuku = ServiceFactory.get_service("mitsuku")
        # while self._running:
        #     message = input(">>")
        #     response = mitsuku.ask_question(bot.client.client_context, message)
        #     print(response)

        bot.initiate_conversation_storage()

        while self._running:
            if self._first_time:
                try:
                    if self._session_saving_mode:
                        client_context = self.load_client_context(self._configuration.client_configuration.default_userid, conversation_file)
                    else:
                        client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
                except Exception as exp:
                    client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
                finally:
                    self._first_time = False

            self._running = self.wait_and_answer(client_context)


    def initial_question(self, request, username):
        question = "session"+str(request.session_number) + " " + username
        return question


    # def worker_run_loop(self):
    #     #todo Needs a major refactor to clean this as much as possible
    #     #todo read the configuration from the programy configuration mechanism
    #     #todo login should be done with Ylogger
    #     #todo save conversations to database
    #     #self.configuration.client_configuration.configurations[0]
    #
    #     root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    #     filepath = os.path.join(root, "bots//ryan//config.yaml")
    #     with open(filepath, encoding="utf-8") as file_reader:
    #         self._yaml_dict = yaml.load(file_reader)
    #
    #     ip = self._yaml_dict["broker"]["ip"]
    #     port = self._yaml_dict["broker"]["port"]
    #     service_name = self._yaml_dict["broker"]["service_name"]
    #
    #
    #     self._running = True
    #     conversation_file = "conv_questions.p"
    #     worker = MajorDomoWorker(str(ip)+":"+str(port), str(service_name))
    #     response = None
    #     client_context = None
    #     session_file = ""
    #     while True:
    #         ### pre dialog computations
    #         request = worker._recv(response)
    #         if request is None:
    #             break  # Worker was interrupted
    #
    #         if request[0] == "ready":
    #             response_string = "ready"
    #             print("command ready")
    #
    #         elif request[0] == "user":
    #             print("command user")
    #             if len(request) > 1:
    #                 session_num = str(request[1])
    #                 username = str(request[2])
    #                 #directory = os.path.join("../../../../results/", username)
    #
    #                 directory = os.path.join(root, "results", username)
    #                 if not os.path.exists(directory):
    #                     os.mkdir(directory)
    #
    #                 session_file = directory+"/session"+session_num
    #                 with open(session_file, 'a') as file_writer:
    #                     file_writer.write("session\n")
    #
    #
    #
    #             if self._first_time:
    #                 try:
    #                     if self._session_saving_mode:
    #                         client_context = self.load_client_context(
    #                             self._configuration.client_configuration.default_userid, conversation_file)
    #                     else:
    #                         client_context = self.create_client_context(
    #                             self._configuration.client_configuration.default_userid)
    #                 except Exception as exp:
    #                     client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
    #                 finally:
    #                     self._first_time = False
    #
    #             #set the bot properties here!
    #             # response = self.process_question(client_context, "bot properties")
    #             # if response == "success":
    #             #     print("bot properties set correctly")
    #             # else:
    #             #     print("there is a problem setting bot properties")
    #             #
    #             # response_string = "user is ready"
    #
    #         elif len(request) > 1 and request[0] == "session":
    #             print("session command")
    #
    #             session_id = request[1]
    #             #username = request[1]
    #             question = "session"+str(session_id)+" "+username
    #             response = self.process_question(client_context, question)
    #             response_dict = self.dictionary_of_response(response)
    #             response_string = str(response_dict)
    #
    #         elif len(request) > 1 and request[0] == "question":
    #             try:
    #                 if client_context is not None:
    #                     question = request[1]
    #                     response = self.process_question(client_context, question)
    #                     response_dict = self.dictionary_of_response(response)
    #                     ####save question and respose to file
    #                     with open(session_file, "a") as file_writer:
    #                         file_writer.write(str(datetime.now()) + " | "+question+" | "+response_dict["conversation"]["response"]+"\n")
    #                     #####
    #                     response_string = str(response_dict)
    #                 else:
    #                     response_string = "client context is None"
    #             except:
    #                 response_string = "chatbot internal failure"
    #
    #         print(response_string)
    #         response = [response_string]
    #         # request = worker.recv(response)
    #         # if request is None:
    #         #     break  # Worker was interrupted
    #         # if "print me" == request:
    #         #     print("Received a command.")


    def dictionary_of_response(self, response, robot):
        answer = ""
        image_filename = ""
        duration = ""
        video_filename = ""
        if robot:

            if robot is not None and "options" in robot and "option" in robot['options']:
                answer = robot['options']['option']


            if robot is not None and "image" in robot and "filename" in robot['image']:
                image_filename = robot['image']['filename']


            if robot is not None and "image" in robot and "duration" in robot["image"]:
                duration = robot["image"]["duration"]


            if robot is not None and "video" in robot and "filename" in robot["video"]:
                video_filename = robot["video"]["filename"]


        return {"conversation":
                    {"question": "",
                     "response": response,
                     "answer": answer
                     },
                "image":
                    {"filename": image_filename,
                     "duration": duration
                     },
                "video":
                    {
                        "filename": video_filename
                    }
                }


    def wait_and_answer(self, client_context):
        raise NotImplementedError("You must override this and implement the logic wait for a question and send an answer back")

    def post_run_loop(self):
        pass

    def run(self):
        #todo refactor to move this out of here
        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
        filepath = os.path.join(root, "bots//ryan//config.yaml")
        with open(filepath, encoding="utf-8") as file_reader:
            self._yaml_dict = yaml.load(file_reader)

        worker_running = self._yaml_dict["broker"]["running"]

        if self.arguments.noloop is False:
            YLogger.info(self, "Entering conversation loop...")

            self.prior_to_run_loop()

            if worker_running:
                self.worker_run_loop()
            else:
                self.run_loop()

            self.post_run_loop()

        else:
            YLogger.debug(self, "noloop set to True, exiting...")
