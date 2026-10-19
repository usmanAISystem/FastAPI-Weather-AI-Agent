# 🌦️ AI Weather Assistant Agent

This is a smart Python application built with *FastAPI* and *LangChain* that utilizes the *Gemini 3.8 Flash* model to fetch and analyze real-time weather information for any city.

---

## 🚀 Features
* *AI-Powered:* Uses Google's Gemini 3.8 Flash model for intelligent responses.
* *LangChain Agents:* Implements function-calling tools to dynamically fetch weather data.
* *Secure Setup:* Uses environment variables to protect API keys and sensitive configuration URLs.
* *FastAPI Backend:* Provides a modern, fast, and scalable API infrastructure.

---

## 📁 Project Structure
text
├── agents/
│   └── help.py            # Contains Gemini configuration and Weather Tool
├── main.py                # FastAPI main application gateway
├── .env                   # Local secret variables (Never commit to GitHub)
├── .env.example           # Template for environment variables
├── .gitignore             # Files to ignore in Git tracking
└── requirements.txt       # Project dependencies


---

## 🛠️ Installation & Setup

Follow these steps to set up and run the project locally on your machine:

### 1. Clone the Repository
bash
git clone https://github.com
cd FastApi-Weather-AI-Agent


### 2. Create and Activate a Virtual Environment
bash
# Create Virtual Environment
python -m venv venv

# Activate Environment (Windows)
venv\Scripts\activate

# Activate Environment (Mac/Linux)
source venv/bin/activate


### 3. Install Dependencies
bash
pip install -r requirements.txt


### 4. Configure Environment Variables
1. Duplicate the .env.example file and rename it to .env.
2. Open the .env file and insert your personal configuration details:

text
WEATHER_API_URL="https://railway.app"
GOOGLE_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"


---

## 💻 Running the Application

Start the FastAPI local server using *Uvicorn*:

bash
uvicorn main:app --reload


Once running, you can access the interactive API documentation (Swagger UI) at:
👉 *http://127.0.0*

---

## 🔒 Security Practices
* The .env file is explicitly included in .gitignore to prevent secret leaks.
* Always use .env.example to guide other developers on setting up their local keys.

---

## 🛠️ Built With
* [FastAPI](https://tiangolo.com) - The web framework.
* [LangChain](https://langchain.com) - Building the AI Agent workflow.
* [Google Gemini](https://google.dev) - Large Language Model engine.