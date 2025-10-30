import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(model="openrouter/openai/gpt-4.1", api_key=os.getenv("OPENROUTER_API_KEY"))


def get_dad_joke():
    return "ddd"


root_agent = Agent(
    model=model,
    name="litellm_dad_joke",
    description="Dad joke agent",
    instruction="""
    You are a helpful assistant that tells dad jokes. You have the following tools and you can only use those tools
    - get_dad_joke
    """,
    tools=[get_dad_joke],
)
