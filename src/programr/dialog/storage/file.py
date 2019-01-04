from programr.dialog.dialog import Sentence
from programr.utils.logging.ylogger import YLogger
import os
import time
from os import listdir
from os.path import isfile, join
from datetime import datetime

from programr.dialog.storage.base import ConversationStorage


class ConversationFileStorage(ConversationStorage):

    def __init__(self, config):
        ConversationStorage.__init__(self, config)
        self._last_modified = None

    def empty(self):
        YLogger.debug(self, "Emptying Conversation Folder")
        try:
            if self._config._dir is not None:
                if os.path.exists(self._config._dir):
                    convo_files = [f for f in listdir(self._config._dir) if isfile(join(self._config._dir, f))]
                    for file in convo_files:
                        fullpath = self._config._dir + os.sep + file
                        YLogger.debug(self, "Removing conversation file: [%s]", fullpath)
                        os.remove(fullpath)
        except Exception as e:
            YLogger.exception(self, "Failed emptying conversation directory [%s]"%self._config._dir, e)

    def create_filename(self, userdir, session_number):
        return userdir + os.path.sep +"session"+session_number +".conv"


    def get_user_dir(self, username):
        user_dir = self._config._dir + os.path.sep + username
        if not os.path.exists(user_dir):
            os.mkdir(user_dir)
        return user_dir

    def save_conversation(self, client_context):
        #client_context.userid
        #client_context.bot.conversations["Console"].questions[-1].sentences[0].words
        #client_context.bot.conversations['Console'].properties
        userid = client_context.userid
        bot_properties = client_context.bot.conversations[userid].properties
        questions = client_context.bot.conversations[userid].questions
        answers = client_context.bot.conversations[userid].answers
        try:
            last_question = questions[-1].sentences
        except Exception as e:
            YLogger.exception(self, "question sentences length is zero", e)
            raise e

        try:
            #todo this doesn't handle good
            last_answer = answers[-1].sentences
        except Exception as e:
            YLogger.exception(self, "answer sentences length is zero", e)
            raise e

        if self._config._dir is not None:
            YLogger.debug(self, "Saving conversation to file")
            #os.path.exists(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))+"\\results")
            if os.path.exists(self._config._dir):
                try:
                    session_number = bot_properties["session_number"]
                    user_name = bot_properties["user_name"].title()
                except Exception as e:
                    #todo change them with default values of session_number and user_name
                    session_number = "1"
                    user_name = "test"
                    YLogger.exception(self, "Failed to get session number", e)

                user_dir = self.get_user_dir(user_name)
                filename = self.create_filename(user_dir, session_number)

                with open(filename, "a", encoding="utf-8") as file_writer:
                    question_sentence_text, answer_sentence_text = self.create_conversation(last_question, last_answer)
                    file_writer.write(str(datetime.now()) +" | " + question_sentence_text + " | " + answer_sentence_text+"\n")



    def create_conversation(self, question, answer):
        question_sentence_text = ""
        for question_sentence in question:
            try:
                if question_sentence.words[-1].endswith('?') or question_sentence.words[-1].endswith(')'):
                    end_sign = ""
                else:
                    end_sign = ". "
            except Exception as e:
                YLogger.exception(self, "Failed to get end_sign ", e)

            question_sentence_text += " ".join(question_sentence.words) +end_sign

        answer_sentence_text = ""
        for answer_sentence in answer:
            try:
                if answer_sentence.words[-1].endswith('?') or answer_sentence.words[-1].endswith(')'):
                    end_sign = ""
                else:
                    end_sign = ". "
            except Exception as e:
                YLogger.exception(self, "Failed to get end_sign ", e)

            answer_sentence_text += " ".join(answer_sentence.words) + end_sign

        return question_sentence_text, answer_sentence_text


    def load_conversation(self, conversation, clientid, restore_last_topic=False):
        #todo implement the load conversation
        pass
        # try:
        #     if self._config._dir is not None:
        #         if os.path.exists(self._config._dir):
        #             filename = self.create_filename(clientid)
        #             if os.path.exists(filename):
        #
        #                 should_open = True
        #                 last_modified = time.ctime(os.path.getmtime(filename))
        #                 if self._last_modified is not None:
        #                     if self._last_modified >= last_modified:
        #                         should_open = False
        #                 self._last_modified = last_modified
        #
        #                 if should_open is True:
        #                     YLogger.debug(self, "Loading Conversation from file")
        #
        #                     with open(filename, "r", encoding="utf-8") as convo_file:
        #                         for line in convo_file:
        #                             if ':' in line:
        #                                 splits = line.split(":")
        #                                 name = splits[0].strip()
        #                                 value = splits[1].strip()
        #                                 if name == "topic":
        #                                     if restore_last_topic is True:
        #                                         YLogger.debug(self, "Loading stored property [%s]=[%s] for %s", name, value, clientid)
        #                                         conversation._properties[name] = value
        #                                 else:
        #                                     YLogger.debug(self, "Loading stored property [%s]=[%s] for %s", name, value, clientid)
        #                                     conversation._properties[name] = value
        #
        # except Exception as e:
        #     YLogger.exception(self, "Failed to load conversation for clientid [%s]"%clientid, e)

    def remove_conversation(self, clientid):
        filename = self.create_filename(clientid)
        if os.path.exists(filename):
            YLogger.debug(self, "Removing conversation for %s", clientid)
            os.path.remove(filename)