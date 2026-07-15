from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

# Define a structured output model for course recommendations
class CourseRecommendation(BaseModel):
  course: str = Field(description="Course name")
  level: str = Field(description="Difficulty level")
  duration_hours: int = Field(description="Estimated duration")
  reason: str = Field(description="Why this course is recommended")
  
# Initialize the model
llm = ChatOpenAI(model="gpt-4o")

# Configure the LLM to use the structured output model
llm = llm.with_structured_output(CourseRecommendation, method="json_schema")

# Invoke the model with a prompt
recommendation = llm.invoke("Recommend a beginner course for learning LangChain.")

# The response is now a structured object we can access its fields directly
print(f"Course: {recommendation.course}") # type: ignore
print(f"Level: {recommendation.level}") # type: ignore
print(f"Duration: {recommendation.duration_hours} hours") # type: ignore
print(f"Reason: {recommendation.reason}") # type: ignore