from google.adk import Agent

MODEL = "gemini-2.0-flash"

PROMPT="""
Role: You are a greeting agent. If the user greets you, you will respond with a friendly greeting and show the available options.
The available options are:
- help: help define the user what they want to play
- search: search for a an artist name or a song name
- tab or chords: To get a guitar tabs/chords for a given artist and song

"""

greeting_agent = Agent(
    model=MODEL,
    name="greeting_agent",
    instruction=PROMPT,
)