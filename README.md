# 🌤️ FastAPI Weather AI Agent

A powerful AI Agent built with FastAPI, LangChain & Gemini that provides real-time weather information for any city using tool calling.

## ✨ Features
- 🤖 AI Agent with tool calling capability
- 🌦️ Real-time weather data for any city
- ⚡ FastAPI powered REST API
- 🧠 Powered by Google Gemini 1.5 Flash
- 📖 Auto-generated Swagger Docs

## 🛠️ Tech Stack
- **Backend:** FastAPI, Uvicorn
- **AI Framework:** LangChain, LangGraph
- **LLM:** ChatGoogleGenerativeAI (Gemini)
- **Weather API:** p2pclouds

## 📁 Project Structure

Fastapi-Agent/
├── agents/
│   └── help.py         # get_weather tool & Agent logic
├── controllers/
│   └── query.py        # Query controller
├── routers/
│   └── ai.py           # API routes
├── main.py             # FastAPI entry point
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md


## 🚀 Installation & Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/FastAPI-Weather-AI-Agent.git
cd FastAPI-Weather-AI-Agent

2. Create venv
python -m venv venv
.\venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Setup .env
Create .env file in root:
GOOGLE_API_KEY=your_gemini_api_key_here

5. Run server
uvicorn main:app --reload

Server: http://127.0.0.1:8000🔗 
🔗API Endpoints
GET / - Welcome message
GET /v1/ai/query/?q=your_question - Ask AI
GET /docs - Swagger Docs

Example:
/v1/ai/query/?q=what is weather of lahore

👨‍💻 Author
Built with ❤️ for learning Agentic AI