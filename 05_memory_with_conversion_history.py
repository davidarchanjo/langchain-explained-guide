from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

# Store for session histories
session_store = {}

# Define the function to retrieve or create a session history
def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

# Prompt now includes a placeholder for chat history
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Remember the conversation context."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

llm = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()

chain = prompt | llm | parser

# Wrap the chain with memory management
chain = RunnableWithMessageHistory(
    chain,  # type: ignore
    get_session_history,
    input_messages_key="question",
    history_messages_key="chat_history"
)

# Session config to identify the conversation
config = {"configurable": {"session_id": "user_david_session"}}

# First message
response1 = chain.invoke(
    {"question": "Hey, David here from Brazil."},
    config=config # type: ignore
)
print(response1)  # "Nice to meet you, David!"

# Second message: now the LLM remembers
response2 = chain.invoke(
    {"question": "What's my home country?"},
    config=config # type: ignore
)
print(response2)  # "Based on what you told me, your home country is Brazil!"