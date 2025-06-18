
from google.adk import Agent
from google.adk.tools import google_search

MODEL = "gemini-2.0-flash"

PROMPT="""
Role: You are a musical search agent. You will search for musical information on the internet.

Tool: You MUST utilize the Google Search tool to gather the most current information. 
Direct access to musical databases is not assumed, so search strategies must rely on effective web search querying.
"""

google_search_agent = Agent(
    model=MODEL,
    name="google_search_agent",
    instruction=PROMPT,
    tools=[google_search],
)