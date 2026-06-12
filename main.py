from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.tools import tool
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

openweather_api_key = os.getenv("OPENWEATHER_API_KEY")

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

@tool
def get_temp_info(city: str):
    """
    Get temperature, humidity, wind speed and weather condition for a city.
    """
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}&units=metric"
    )

    data = response.json()

    return {
        "city": city,
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "weather": data["weather"][0]["description"]
    }

class WeatherRequest(BaseModel):
    city: str
    question: str


@app.post("/get_weather")
def get_weather(data: WeatherRequest):
    try:
        weather = get_temp_info.invoke(data.city)

        prompt = f"""
        Weather Data:
        {weather}

        User Question:
        {data.question}
        """

        result = llm.invoke(prompt)

        return {
            "msg": {
                **weather,
                "answer": result.content
            }
        }

    except Exception as e:
        return {
            "error": str(e)
        }