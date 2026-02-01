from crewai import Agent, LLM
from tools import yt_tool  # Changed from yt_tools to yt_tool

groq_llm = LLM(
    model="groq/llama3-70b-8192",
    api_key="YOUR_ACTUAL_GROQ_API_KEY", # Or use os.getenv("GROQ_API_KEY")
    temperature=0.7  # Fixed spelling
)

blog_researcher = Agent(
    role='Blog researcher from youtube videos', # Added comma
    goal='get the relevant video transcript for the topic {topic}',
    verbose=True,
    memory=True,
    backstory="Expert in AI/ML research and video analysis",
    tools=[yt_tool], # Added comma
    llm=groq_llm
)

blog_writer = Agent(
    role='Blog writer', # Added comma
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory="Expert in simplifying complex topics",
    tools=[yt_tool],
    llm=groq_llm,
    allow_delegation=False
)