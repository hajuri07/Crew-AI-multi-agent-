from crewai_tools import YoutubeVideoSearchTool


yt_tool = YoutubeVideoSearchTool(
    youtube_video_url="https://youtu.be/3b--y2QjH3s?si=7xtZ1Cm6ZJ270y8b",
    config=dict(
        llm=dict(
            provider="groq", # Use Groq instead of OpenAI
            config=dict(model="llama3-8b-8192"),
        ),
        embedder=dict(
            provider="huggingface", # Use HuggingFace (No API key needed for this part!)
            config=dict(model="sentence-transformers/all-MiniLM-L6-v2"),
        ),
    )
)