from langchain_openai import ChatOpenAI

# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Invoke the model with a simple prompt
response = llm.invoke("What is LangChain in one sentence?")

print(response.content)
