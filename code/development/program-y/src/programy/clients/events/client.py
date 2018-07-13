"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from programy.config.file.yaml_file import YamlConfigurationFile
from programy.utils.logging.ylogger import YLogger

from programy.clients.client import BotClient
from programy.majordomo.mdwrkapi import MajorDomoWorker

import os
from datetime import datetime

class EventBotClient(BotClient):

    def __init__(self, id, argument_parser=None):
        self._running = False
        self._first_time = True
        self._session_saving_mode = False
        BotClient.__init__(self, id, argument_parser=argument_parser)

    def prior_to_run_loop(self):
        pass

    def run_loop(self):
        #client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
        self._running = True
        conversation_file = "/home/rohola/conv_questions.p"
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




    def worker_run_loop(self):
        #todo Needs a major refactor to clean this as much as possible
        #todo read the configuration from the programy configuration mechanism
        #self.configuration.client_configuration.configurations[0]

        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
        import yaml
        filepath = os.path.join(root, "bots//tutorial//config.yaml")
        with open(filepath, encoding="utf-8") as file_reader:
            self._yaml_dict = yaml.load(file_reader)

        ip = self._yaml_dict["broker"]["ip"]
        port = self._yaml_dict["broker"]["port"]
        service_name = self._yaml_dict["broker"]["service_name"]


        self._running = True
        conversation_file = "/home/rohola/conv_questions.p"
        worker = MajorDomoWorker(str(ip)+":"+str(port), str(service_name))
        response = None
        client_context = None
        session_file = ""
        while True:
            ### pre dialog computations
            request = worker.recv(response)
            if request is None:
                break  # Worker was interrupted

            if request[0] == "ready":
                response_string = "ready"
                print("$$$$$$$$$$$$$ready$$$$$$$$$$$")

            elif request[0] == "user":
                if len(request) > 1:
                    session_num = str(request[1])
                    username = str(request[2])
                    #directory = os.path.join("../../../../results/", username)

                    directory = os.path.join(root, "results", username)
                    if not os.path.exists(directory):
                        os.mkdir(directory)

                    session_file = directory+"/session"+session_num
                    with open(session_file, 'w') as file_writer:
                        file_writer.write("session\n")



                if self._first_time:
                    try:
                        if self._session_saving_mode:
                            client_context = self.load_client_context(
                                self._configuration.client_configuration.default_userid, conversation_file)
                        else:
                            client_context = self.create_client_context(
                                self._configuration.client_configuration.default_userid)
                    except Exception as exp:
                        client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
                    finally:
                        self._first_time = False



                response_string = "user is ready"

            elif len(request) > 1 and request[0] == "session":
                session_id = request[1]
                username = request[1]
                question = "session"+str(session_id)+" "+username
                response = self.process_question(client_context, question)
                response_dict = self.dictionary_of_response(response)
                response_string = str(response_dict)

            elif len(request) > 1 and request[0] == "question":
                try:
                    if client_context is not None:
                        question = request[1]
                        response = self.process_question(client_context, question)
                        response_dict = self.dictionary_of_response(response)
                        ####save question and respose to file
                        with open(session_file, "a") as file_writer:
                            file_writer.write(str(datetime.now()) + " | "+question+" | "+response_dict["conversation"]["response"]+"\n")
                        #####
                        response_string = str(response_dict)
                    else:
                        response_string = "client context is None"
                except:
                    response_string = "chatbot internal failure"


            response = [response_string]
            # request = worker.recv(response)
            # if request is None:
            #     break  # Worker was interrupted
            # if "print me" == request:
            #     print("Received a command.")




    def dictionary_of_response(self, response):
        answers = []
        image_filename = ""
        duration = ""
        video_filename = ""
        response_part = ""
        if "(" in response:
            parts = response.split("(")
            response_part = parts[0]
            answers = parts[1].split(")")[0].split("|")

        if "#" in response:
            parts = response.split("#")
            response = parts[0]
            if "image" in parts[1]:
                image = parts[1].strip("#").split(",")[0]
                image_filename = image.split(":")[1]
                if len(parts[1].strip("#").split(",")) > 1:
                    duration = parts[1].strip("#").split(",")[1]
                    duration = duration.split(":")[1]

            if "video" in parts[1]:
                video_filename = parts[1].strip("#").split(",")[0]

        if "#" not in response and "(" not in response:
            response_part = response

        return {"conversation":
                    {"question": "",
                     "response": response_part,
                     "answer": answers
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

        if self.arguments.noloop is False:
            YLogger.info(self, "Entering conversation loop...")

            self.prior_to_run_loop()

            self.run_loop()
            #self.worker_run_loop()

            self.post_run_loop()

        else:
            YLogger.debug(self, "noloop set to True, exiting...")



if __name__ == "__main__":
    # directory = "../../../../results/" + "kate" + "/"
    # if not os.path.exists(directory):
    #     os.mkdir(directory)
    # print(os.path.dirname(__file__))
    # root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    # directory = os.path.join(root, "results", "kate")
    # if not os.path.exists(directory):
    #     os.mkdir(directory)
    #     print("done")
    ob = ""
    if ob is not None:
        print("yes")