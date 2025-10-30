from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-2.0-flash",
    name="structured_output_agent",
    description="Structured output agent",
    instruction="""
    You are a helpful assistant
    """,
)
