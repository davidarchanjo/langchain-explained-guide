from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Define the prompt structure once
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Always respond in valid JSON."),
    ("human", "{question}")
])

# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Initialize the output parser
parser = JsonOutputParser()

# Create a chain that combines the prompt template, the model, and the output parser
chain = prompt | llm | parser

# Invoke with a dynamic question
response = chain.invoke({
    "question": "Give me three benefits of LangChain as a JSON array with 'title' and 'description' fields. Items in the JSON array must be sorted alphabetically by the 'title' field."
})

# Now the response is a Python list we can iterate over
for benefit in response:
    print(f"- {benefit['title']}: {benefit['description']}")