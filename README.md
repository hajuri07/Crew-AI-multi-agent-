##🤖 YouTube-to-Blog AI Agent (Practice Project
This is a practice project built using CrewAI and Groq to automate the process of researching YouTube videos and turning them into engaging blog posts.

📁 Project Structure
The project is split into modular files for better organization:

tools.py: Contains the YoutubeVideoSearchTool configured for a specific video URL.

agents.py: Defines the Blog Researcher and Blog Writer agents using the Llama 3 model via Groq.

tasks.py: Outlines the specific research and writing assignments for the agents.

crew.py: The main entry point that assembles the crew and kicks off the process.

🚀 Technologies Used
Framework: CrewAI

LLM: Groq (Llama 3-70b)

Tools: CrewAI YouTube Search Tool

Environment: Google Colab

🛠️ Setup & Installation
Install Dependencies:

Bash
pip install -U 'crewai[tools]' langchain-groq python-dotenv
Environment Variables: Ensure you have your Groq API Key set up in your environment:

Python
os.environ["GROQ_API_KEY"] = "your_groq_api_key"
📝 How to Run
In your Google Colab notebook, ensure all .py files are in the /content directory and run:

Python
python crew.py
The output will be generated as a Markdown file named new-blog-post.md.
