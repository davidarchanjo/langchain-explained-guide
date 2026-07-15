import platform
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool

# Define the tools that the agent can use
@tool
def get_current_time() -> str:
    """Return the current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def get_operating_system() -> str:
    """Returns the name and architecture of the host operating system.
    
    Use this tool whenever the user asks about their system environment, 
    OS name, computer platform, or machine architecture.
    """
    os_name = platform.system()
    architecture = platform.machine()
    
    return f"Operating System: {os_name}, Architecture: {architecture}"

tools = [get_current_time, get_operating_system]

# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Define the prompt structure
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use tools whenever they are useful."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# Build the agent and executor
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Example usage
input = "What time is it right now?"
response = agent_executor.invoke({"input": input})
print(f"{input}:", response["output"])

input = "What is today's date?"
response = agent_executor.invoke({"input": input})
print(f"{input}:", response["output"])

input = "What platform is the user running on?"
response = agent_executor.invoke({"input": input})
print(f"{input}:", response["output"])