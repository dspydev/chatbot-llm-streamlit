import openai

def get_chatbot_response(openai_api_key, messages, prompt):
    """
    This function takes an OpenAI API key, a list of previous messages, and a user prompt as input.
    It uses OpenAI's GPT-3 model to generate a response to the user's prompt.
    """
    # Set the OpenAI API key
    openai.api_key = openai_api_key

    # Add the user's message to the list of messages
    messages.append({"role": "user", "content": prompt})

    # Get a response from OpenAI's GPT-3 model
    response = openai.Completion.create(
        engine="davinci",
        prompt=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response_text = response["choices"][0]["text"]

    # Add the assistant's message to the list of messages
    messages.append({"role": "assistant", "content": response_text})

    # Return the assistant's message
    return response_text
