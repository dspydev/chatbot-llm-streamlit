import unittest
from unittest.mock import patch
from chatbot_llm_logic_and_function import get_chatbot_response

class TestGetChatbotResponse(unittest.TestCase):
    @patch("openai.Completion.create")
    def test_get_chatbot_response(self, mock_create):
        # Set up the mock response from OpenAI's GPT-3 model
        mock_create.return_value = {
            "choices": [
                {
                    "text": "I'm doing well, thank you. How can I help you?"
                }
            ]
        }

        # Call the get_chatbot_response function with test inputs
        openai_api_key = "test-api-key"
        messages = []
        prompt = "Hello, how are you?"
        response = get_chatbot_response(openai_api_key, messages, prompt)

        # Check that the response is correct
        self.assertEqual(response, "I'm doing well, thank you. How can I help you?")

if __name__ == "__main__":
    unittest.main()
