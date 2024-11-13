import streamlit as st
from bank_chatbot import route_query, client

# Set up the title and introductory text
st.title("24/7 Banking Chatbot")
st.write("Ask me about banking services, loan eligibility, account support, and more.")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Create input box for user queries
user_input = st.text_input("Type your question here:")

# When the "Send" button is clicked
if st.button("Send") and user_input:
    # Get the response from the appropriate agent
    response = route_query(client, user_input)
    
    # Append user query and response to chat history
    st.session_state.chat_history.append(("User", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "User":
        st.write(f"**You**: {message}")
    else:
        st.write(f"**Bot**: {message}")
