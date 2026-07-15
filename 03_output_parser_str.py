from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Initialize the output parser
parser = StrOutputParser()

# Create a chain that combines the model and the output parser
chain = llm | parser

# Invoke the chain with a simple prompt
response = chain.invoke("Explain what a Vector database is.")

print(type(response)) # <class 'langchain_core.messages.base.TextAccessor'>
print(response)       # A vector database is a specialized database...