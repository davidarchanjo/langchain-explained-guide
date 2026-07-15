from langchain.chat_models import init_chat_model

model = init_chat_model(model="gpt-4o", model_provider="openai")

response = model.invoke("Explain LangChain in simple technical terms in under 100 words")

print(response.content)