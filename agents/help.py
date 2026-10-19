from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import requests

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    res= requests.get(f"https://p2pclouds.up.railway.app/v1/learn/weather?city={city}")

    data=res.json()
    return data

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

helping_agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)
