from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Define a structured output model for course recommendations
class CourseRecommendation(BaseModel):
  course: str = Field(description="Course name")
  level: str = Field(description="Difficulty level")
  duration_hours: int = Field(description="Estimated duration")
  reason: str = Field(description="Why this course is recommended")
  
# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Initialize the Pydantic parser for the structured output model
parser = PydanticOutputParser(pydantic_object=CourseRecommendation)

# Define the prompt structure with format instructions for the Pydantic parser
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI education advisor.

Return ONLY valid JSON.

{format_instructions}
"""
    ),
    (
        "human",
        "Recommend a {level} course for learning {topic}."
    )
])

# Create a chain that combines the prompt template, the model, and the Pydantic output parser
chain = prompt | llm | parser

# Invoke with dynamic values and format instructions
recommendation = chain.invoke({"topic": "LangChain", "level": "beginner", "format_instructions": parser.get_format_instructions()})

# The response is a structured object we can access its fields directly
print(f"Course: {recommendation.course}") # type: ignore
print(f"Level: {recommendation.level}") # type: ignore
print(f"Duration: {recommendation.duration_hours} hours") # type: ignore
print(f"Reason: {recommendation.reason}") # type: ignore