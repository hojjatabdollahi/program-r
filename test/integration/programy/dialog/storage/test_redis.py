import unittest

from programr.config.bot.redisstorage import BotConversationsRedisStorageConfiguration
from programr.dialog.storage.redis import ConversationRedisStorage
from programrtest.aiml_tests.client import TestClient
from programr.dialog.dialog import Conversation, Question


class ConversationRedisStorageTests(unittest.TestCase):

    def test_persistence(self):

        storage_config = BotConversationsRedisStorageConfiguration("redis")
        redis = ConversationRedisStorage(storage_config)
        self.assertIsNotNone(redis)

        client = TestClient()
        client_context = client.create_client_context("testid")
        conversation1 = Conversation(client_context)
        conversation1.set_property("topic", "topic1")

        question = client_context.bot.get_question(client_context, "hello", srai=False)
        conversation1.record_question(question)

        redis.save_conversation(conversation1, client_context.userid)

        conversation2 = Conversation(client_context)
        redis.load_conversation(conversation2, client_context.userid)
        self.assertIsNotNone(conversation2)
        self.assertIsNotNone(conversation2.properties)

        self.assertEquals(conversation1.properties, conversation2.properties)

