import openai
import streamlit as st

def main():
    """
    This is a Streamlit app that uses OpenAI's GPT-3 to create a chatbot.
    """
    with st.sidebar:
        # The Streamlit sidebar allows you to add widgets and other content to the left side of the app.
        # In this case, we are using the sidebar to get the OpenAI API key from the user and provide instructions on how to get one.

        # Use a heading to introduce the OpenAI API key section
        st.subheader("OpenAI API Key")

        # Get the OpenAI API key from the user
        openai_api_key = st.text_input("Enter your API key", key="chatbot_api_key", type="password")
        # Provide a clickable link to get an API key
        st.markdown("Get an OpenAI API key at https://platform.openai.com/account/api-keys")

        # Use a heading to introduce the instructions section
        st.subheader("Instructions")

        # Provide step-by-step instructions on how to get an OpenAI API key
        st.write("To obtain an OpenAI API key, follow these steps:")
        st.write("1. Go to the OpenAI website.")
        st.write("2. Click on the 'Sign up' button in the top right corner of the page.")
        st.write("3. Fill out the sign-up form with your information and click on the 'Create account' button.")
        st.write("4. Once your account is created, log in and go to the API keys page.")
        st.write("5. Click on the 'Create new API key' button and follow the instructions to create a new API key.")

    # Set the title of the app
    st.title("💬 Chatbot")

    # Display a welcome message
    st.write("Welcome to the chatbot! To get started, enter your OpenAI API key in the sidebar, and then type a message in the chat box below.")

    # Initialize the messages in the session state if they don't exist
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display the messages in the chat
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Get input from the user
    if prompt := st.chat_input():
        # Check if the OpenAI API key is provided
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        try:
            # Set the OpenAI API key
            openai.api_key = openai_api_key

            # Add the user's message to the session state and display it in the chat
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            # Get a response from OpenAI's GPT-3 model
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
            msg = response.choices[0].message

            # Add the assistant's message to the session state and display it in the chat
            st.session_state.messages.append(msg)
            st.chat_message("assistant").write(msg.content)
        except Exception as e:
            # Handle any errors that may occur
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
