from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Initialize the output parser
parser = StrOutputParser()

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant who answers questions in a conversational manner."),
    ("human", "{user_input}"),
])

# Create the chain
chain = prompt | llm | parser

# Continuously interact with the user
while True:
    # Get user input
    user_input = input("You: ")

    # Break the loop if the user types "exit" or "quit"
    if user_input.lower() in {"exit", "quit"}:
        break

    # Stream the response token by token
    print("\nAssistant: ", end="", flush=True)
    for chunk in chain.stream({"user_input": user_input}):
        print(chunk, end="", flush=True)
    print("\n")