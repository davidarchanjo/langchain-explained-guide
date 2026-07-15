from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("""
    You are a helpful assistant.
    Explain {concept} in simple technical terms in under 100 words.
""")

model = init_chat_model(model="gpt-4o", model_provider="openai")

prompt = prompt_template.format(concept="LangGraph")

response = model.invoke(prompt)

print(response.content)