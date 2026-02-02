🤖 YouTube-to-Blog AI Agent
(Practice Project using CrewAI & Groq)

This project demonstrates a simple multi-agent AI system that converts a YouTube video into a well-structured blog post.

It was built purely for practice to understand how AI agents collaborate, use tools, and complete tasks using large language models. This is not a production-grade application.


==================================================
📌 Project Overview
==================================================

The YouTube-to-Blog AI Agent automates the following workflow:

1. Takes a YouTube video URL as input
2. An AI Research Agent analyzes the video content
3. An AI Writing Agent transforms the research into a blog post
4. The final blog is saved as a Markdown file

This project focuses on learning agent orchestration rather than performance or scale.


==================================================
🧠 How It Works
==================================================

- The Research Agent extracts key points, themes, and insights from the YouTube video
- The Writing Agent uses this research to generate a readable and structured blog
- CrewAI manages task execution and agent collaboration
- Groq (Llama 3-70B) powers all language generation


==================================================
📁 Project Structure
==================================================

.
├── tools.py
│   - Defines the YouTube search tool for a specific video URL
│
├── agents.py
│   - Contains definitions for:
│     • Blog Researcher Agent
│     • Blog Writer Agent
│   - Uses Groq with the Llama 3-70B model
│
├── tasks.py
│   - Defines research and writing tasks assigned to agents
│
├── crew.py
│   - Main entry point that initializes the crew and runs the workflow


==================================================
🚀 Technologies Used
==================================================

- Framework: CrewAI
- LLM Provider: Groq
- Model: Llama 3-70B
- Tools: CrewAI YouTube Search Tool
- Environment: Google Colab


==================================================
🛠️ Setup & Installation
==================================================

Step 1: Install Required Dependencies

pip install -U 'crewai[tools]' langchain-groq python-dotenv


Step 2: Configure Environment Variables

Set your Groq API key in the environment:

import os
os.environ["GROQ_API_KEY"] = "your_groq_api_key"


==================================================
▶️ How to Run the Project
==================================================

1. Upload all project files (.py) into the /content directory in Google Colab
2. Run the main script:

python crew.py


==================================================
📝 Output
==================================================

- The generated blog post is saved as:
  new-blog-post.md

- Output format:
  Markdown (.md)

- Content:
  A blog article generated from the YouTube video analysis


==================================================
⚠️ Important Notes
==================================================

- This project was built only for practice and learning purposes
- Main learning goals:
  - Multi-agent AI design
  - Task delegation using CrewAI
  - Tool integration with LLMs
- Not optimized for real-world deployment


==================================================
💡 Future Improvements
==================================================

- Accept multiple YouTube URLs
- Add SEO-focused blog generation
- Export blogs to HTML or CMS formats
- Add a simple UI using Streamlit
