from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the target document
loader = TextLoader("./assets/company_credentials.txt")
documents = loader.load()

# Split into smaller chunks for better retrieval
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Initialize the embedding model
embeddings = OpenAIEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:8001/v1",
    check_embedding_ctx_length=False
)

# Generate embeddings and index them in Chroma
vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings)

# Create a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# Build the RAG chain
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful assistant.

Answer the user's question using only the context provided below.

If the answer cannot be found in the context, simply say that you don't know.

Context:
{context}
"""
    ),
    ("human", "{question}")
])

llm = ChatOpenAI(model="gpt-4o")

parser = StrOutputParser()

chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | parser
)

# Query the knowledge base
response = chain.invoke("What are my login credentials for Jira?")

print(response)