import os
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import requests

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    base_url =os.getenv("WEATHER_API_URL") # paste url in .env file
    res= requests.get(f"{base_url}?city={city}")

    data=res.json()
    return data

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"), # paste google genai api key in .env file
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
