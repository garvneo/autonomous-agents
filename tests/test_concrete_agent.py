import asyncio
import random
import unittest
import unittest.mock as mock

from agents.autonomous_agent import AutonomousAgent
from agents.concrete_agent import ConcreteAgent


class TestAutonomousAgent(unittest.TestCase):
    @staticmethod
    def create_agent():
        return AutonomousAgent()

    async def test_consume_messages_empty_queue(self):
        agent = self.create_agent()
        await asyncio.sleep(1)  # Give some time for potential processing
        self.assertFalse(agent.consume_messages.done())

    async def test_consume_messages_with_message(self):
        agent = self.create_agent()
        message = {"type": "test"}
        agent.inbox.put_nowait(message)
        with mock.patch.object(agent, "handle_message") as mock_handle_message:
            await agent.consume_messages()  # Await here
            await asyncio.sleep(0.1)  # Give some time for message processing
            mock_handle_message.assert_called_once_with(message)

    async def test_handle_message_with_handler(self):
        agent = self.create_agent()
        message = {"type": "test"}
        handler = mock.Mock()
        agent.register_message_handler(message["type"], handler)
        await agent.handle_message(message)  # Await here
        await asyncio.sleep(0.1)  # Give some time for message processing
        handler.assert_called_once_with(message)

    async def test_emit_message(self):
        agent = self.create_agent()
        queue = asyncio.Queue()
        agent.outbox = queue
        message = {"data": "test"}
        await agent.emit_message(message)  # Await here
        self.assertEqual(queue.get_nowait(), message)

    def test_register_message_handler(self):
        agent = self.create_agent()
        message_type = "test"
        agent.register_message_handler(message_type, lambda msg: None)
        self.assertEqual(
            agent.message_handlers[message_type], lambda msg: None
        )

    def test_register_behavior(self):
        agent = self.create_agent()
        agent.register_behavior(lambda: None)
        self.assertIn(lambda: None, agent.behaviors)


class TestConcreteAgent(unittest.TestCase):
    def create_agent(self):
        return ConcreteAgent()

    async def test_handle_custom_message_with_hello(self):
        agent = self.create_agent()
        with mock.patch.object(agent.logger, "info") as mock_logger_info:
            message = {"type": "custom", "content": "hello world"}
            await agent.handle_custom_message(message)  # Await here
            mock_logger_info.assert_called_once_with(
                "Received message: %s", message
            )

    async def test_handle_custom_message_without_hello(self):
        agent = self.create_agent()
        message = {"type": "custom", "content": "no hello"}
        await agent.handle_custom_message(
            message
        )  # Await here, No assertion needed

    async def test_generate_random_message(self):
        agent = self.create_agent()
        with mock.patch.object(random, "sample") as mock_sample:
            mock_sample.return_value = ["hello", "world"]
            await agent.generate_random_message()  # Await here
            message = agent.outbox.get_nowait()
            self.assertEqual(message["type"], "custom")
            self.assertEqual(message["content"], "hello world")


if __name__ == "__main__":
    asyncio.run(unittest.main())
