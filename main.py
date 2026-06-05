from fastapi import FastAPI,Query
from langchain_groq import ChatGroq
import os
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()
app = FastAPI()

openweather_api_key = os.getenv("OPENWEATHER_API_KEY")


llm=ChatGroq(
    api_key = os.getenv("GROQ_API_KEY"),
    model = "llama-3.3-70b-versatile"
)

@tool
def get_temp_info(city:str):
    """
    this is to get the temperature details
    """
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}")
    data=response.json()
    return data

agent=create_agent(
    model=llm,
    tools=[get_temp_info]
)

@app.post("/")
def home():
    return {
        "msg":"backend Successfuly running"
    }


@app.post("/get_weather")
def incoming_parametrs(
    city:str = Query(...),
    question:str = Query(...)
):
    result = agent.invoke({
        "msg":[{
            "role":"user",
            "content":f"city:{city} question{question}"
        }]
    })

    return result
    
