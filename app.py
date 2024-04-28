import streamlit as st
from llm import ask_llm


st.set_page_config(page_title='AI-chatbot')
st.title('Chat with your AI Assistant!')


message = st.chat_message('Assistant')
message.write('Hello, Saeed!')
message.write('How can I help you today?')

#initialize the chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    st.chat_message(message['user']).write(message['message'])

prompt = st.chat_input('What\'s up?')
if prompt:
    st.chat_message('User').write(prompt)
    # prepare query for LLM using all historical chat
    query = ''
    for message in st.session_state.chat_history[-5:]:
        query += message['user'] + ': ' + message['message'] + '\n'
    query += "From the above conversation context between user and AI assistant, "
    query += f"answer the following question from user:\n{prompt}"

    print(query)
    response = ask_llm(query)

    st.chat_message('Assistant').write(response)

    st.session_state.chat_history.append({'user': 'User', 'message': prompt})
    st.session_state.chat_history.append({'user': 'Assistant', 'message': response})
    