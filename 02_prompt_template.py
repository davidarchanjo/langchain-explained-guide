from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt structure once
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful technical writer who explains concepts simply."),
    ("human", "Explain {topic} in simple terms. Answer in {language}.")
])

# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Create a chain that combines the prompt template and the model
chain = prompt | llm

# Invoke with dynamic values
response = chain.invoke({"topic": "LangChain", "language": "Portuguese"})

print(response.content)