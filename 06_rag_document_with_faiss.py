from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the knowledge base
loader = TextLoader("./assets/company_credentials.txt")
documents = loader.load()

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Connect to the embedding model and index the document chunks in FAISS
embeddings = OpenAIEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:8001/v1",
    check_embedding_ctx_length=False # Disable client-side token length validation because the local embedding server handles it
)
vector_store = FAISS.from_documents(chunks, embeddings)

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

llm = ChatOpenAI(
    model="gpt-4o",
    base_url="http://localhost:8000/v1"
)

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