from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Initialize the output parser
parser = StrOutputParser()

# Initialize the prompt template to be used with dynamic questions
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

# Create the chain combining the prompt template, the model, and the output parser
chain = prompt | llm | parser

# Stream the response token by token
for chunk in chain.stream({"question": "Explain LangChain in 3 sentences."}):
    print(chunk, end="", flush=True)