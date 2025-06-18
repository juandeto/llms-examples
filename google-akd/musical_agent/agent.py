from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .tools.get_guitar_tabs_and_chords import get_guitar_tabs_and_chords
from .sub_agents.google_search_agent import google_search_agent
from .sub_agents.greeting_agent import greeting_agent

MODEL = "gemini-2.0-flash"

PROMPT='''
    You are a musical agent that provides help for musicians who want to play their favorite songs on their instruments. 
    It can help with song lyrics, guitar tabs, chord progressions and more.
    When the user asks for help or just says Hi, you can provide a list of available options with the greeting_agent.
    When the user asks for a search, you can use the google_search_agent to search for the artist or song name.
    When the user asks for a guitar tab or chords, you can use the guitar_tab_and_chords_agent to get the guitar tab or chords.
    
    **Tool use**
    When using get_guitar_tabs_and_chords tool you must send the following parameters:
        artist (str): The artist name
        song (str): The song name
    Returns:
        str: The guitar tab and chord progression for the given artist and song
'''

musical_agent = LlmAgent(
    name="musical_agent",
    model=MODEL,
    description=(
        "A musical agent that"
        "provides help for musicians who want to play their favorite "
        "songs on their instruments. It can help with song lyrics, "
        "guitar tabs, chord progressions and more"
    ),
    instruction=PROMPT,
    tools=[
        AgentTool(agent=greeting_agent),
        AgentTool(agent=google_search_agent),
        get_guitar_tabs_and_chords,
    ],
)

root_agent = musical_agent