from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Initialize the output parser
parser = StrOutputParser()

# Set two separate chains
summary_chain = (
    ChatPromptTemplate.from_template("Summarize this topic in one sentence: {topic}")
    | llm
    | parser
)

example_chain = (
    ChatPromptTemplate.from_template("Give one practical example of: {topic}")
    | llm
    | parser
)

# Run both chains in parallel and combine the results
chain = RunnableParallel(summary=summary_chain, example=example_chain)

result = chain.invoke({"topic": "LangChain"})

print("Summary:", result["summary"])
print("Example:", result["example"])