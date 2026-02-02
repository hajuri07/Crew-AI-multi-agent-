🤖 YouTube-to-Blog AI Agent (Practice Project)

This is a practice project built using CrewAI and Groq that automates the process of researching a YouTube video and converting it into a structured, engaging blog post.

The main purpose of this project is learning and experimentation with multi-agent AI systems, tool usage, and LLM orchestration. It is not intended to be a production-ready system.


==================================================
📌 What This Project Does
==================================================

- Takes a YouTube video URL as input
- Uses an AI Research Agent to extract key ideas and insights
- Uses an AI Writer Agent to convert research into a blog post
- Saves the final output as a Markdown (.md) file


==================================================
📁 Project Structure
==================================================

The project is organized into modular files for clarity and learning:

.
├── tools.py
│   - Contains the YouTubeVideoSearchTool configured for a specific video
│
├── agents.py
│   - Defines the Blog Researcher and Blog Writer agents
│   - Uses Groq with the Llama 3-70B model
│
├── tasks.py
│   - Defines research and writing tasks assigned to agents
│
├── crew.py
│   - Main entry point that assembles the crew and runs the workflow


==================================================
🚀 Technologies Used
==================================================

- Framework: CrewAI
- LLM: Groq (Llama 3-70B)
- Tools: CrewAI YouTube Search Tool
- Environment: Google Colab


==================================================
🛠️ Setup & Installation
==================================================

Step 1: Install Dependencies

Run the following command in your environment:

pip install -U 'crewai[tools]' langchain-groq python-dotenv


Step 2: Set Environment Variables

Ensure your Groq API key is set in the environment:

import os
os.environ["GROQ_API_KEY"] = "your_groq_api_key"


==================================================
▶️ How to Run
==================================================

1. Upload all .py files to the /content directory in Google Colab
2. Run the main script using:

python crew.py


==================================================
📝 Output
==================================================

- The generated blog post is saved as:
  new-blog-post.md

- Output format:
  Markdown (.md)

- Content:
  A structured blog article derived from the YouTube video


==================================================
⚠️ Notes
==================================================

- This project was created purely for practice and learning
- Focus areas include:
  - Multi-agent workflows
  - Task orchestration
  - Tool integration with LLMs
- Not optimized for scalability or production deployment


==================================================
💡 Possible Future Improvements
==========================================
