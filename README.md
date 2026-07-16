# LangChain Explained Guide

A collection of practical, self-contained Python examples demonstrating the most important concepts in **LangChain**.

This repository is the companion codebase for my [**LangChain Explained Guide**](https://dev.to/davidarchanjo/langchain-explained-a-practical-guide-for-beginners-38jn), where I walk through the core concepts of LangChain with explanations and best practices. Every example in the guide has a corresponding runnable Python implementation in this repository, allowing you to experiment with the code while reading.

Whether you're new to LangChain or looking for concise examples of specific features, this repository is designed to serve as a hands-on learning resource.

## Features
- Prompt templates
- Output parsers
  - String output
  - JSON output
  - Structured output (Pydantic)
  - Native structured responses
- LCEL (LangChain Expression Language)
  - Basic chains
  - Branching
  - Parallel execution
  - Streaming
- Conversation memory
- Retrieval-Augmented Generation (RAG)
  - Chroma vector database
  - FAISS vector database
- Tool calling
- Local and cloud LLM support

---

## Requirements
- Python 3.10+
- OpenAI-compatible language model

Install the dependencies:
```bash
pip install -r requirements.txt
```

---

## Configure the LLM
Most examples use the `ChatOpenAI` interface, which can connect to:
- OpenAI
- Ollama
- vLLM
- LM Studio
- llama.cpp server
- Any OpenAI-compatible endpoint

Example:
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed",
    model="your-model-name",
)
```

If using OpenAI directly:
```bash
export OPENAI_API_KEY=<your-api-key>
```

---

## Examples

### 01 - Hello World
The simplest possible LangChain application.

Concepts:
- Chat models
- Invoking an LLM

---

### 02 - Prompt Templates
Demonstrates how to create reusable prompts using `ChatPromptTemplate`.

Concepts:
- Prompt variables
- Prompt composition
- Message templates

---

### 03 - Output Parsers
Examples of transforming raw LLM responses into structured data.

Includes:
- `StrOutputParser`
- JSON output
- Pydantic models
- Native structured responses

---

### 04 - LCEL (LangChain Expression Language)
Examples covering the core LCEL operators.

Includes:
- Sequential chains
- Batch processing
- Parallel execution
- Conditional branching
- Streaming responses

---

### 05 - Conversation Memory
Shows how to maintain conversation history across multiple interactions.

Concepts:
- Message history
- Stateful conversations
- RunnableWithMessageHistory

---

### 06 - Retrieval-Augmented Generation (RAG)
Demonstrates how to build a simple RAG pipeline using local vector databases.

Examples:
- ChromaDB
- FAISS

Concepts:
- Document loading
- Text splitting
- Embeddings
- Similarity search
- Retrieval chains

---

### 07 - Tool Calling
Demonstrates how an LLM can invoke Python functions as tools.

Concepts:
- `@tool`
- Tool binding
- Function calling
- Agent workflows

---

## Recommended Learning Order
1. Hello World
2. Prompt Templates
3. Output Parsers
4. LCEL
5. Conversation Memory
6. RAG
7. Tool Calling

Following this sequence provides a gradual introduction from basic LLM interactions to more advanced LangChain workflows.

---

## Technologies
- Python
- LangChain
- LangChain OpenAI
- ChromaDB
- FAISS
- Pydantic

---

## License
This repository is intended for educational purposes.