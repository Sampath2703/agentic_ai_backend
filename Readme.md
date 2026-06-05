# 🚀 AI Weather Forecast Agent (Full Stack AI Project)

An AI-powered weather forecasting assistant built using **Streamlit, FastAPI, LangChain, Groq LLaMA 3.3 70B, and OpenWeather API**.  
This project provides **real-time weather data + AI-generated suggestions** based on user queries.

---

# 📌 Project Overview

The AI Weather Forecast Agent is a full-stack intelligent application that:

- Fetches real-time weather data from OpenWeather API
- Uses AI (Groq LLaMA 3.3) to analyze weather conditions
- Answers user questions like:
  - “Is it safe to ride a bike?”
  - “Should I carry an umbrella?”
  - “Is it too hot for travel?”

It combines **live weather data + AI reasoning** into a single intelligent response.

---

# 🎯 Key Features

## 🌦️ Real-Time Weather Data
- Temperature
- Humidity
- Wind Speed
- Weather Condition

## 🧠 AI-Powered Weather Assistant
- Uses **Groq LLaMA 3.3 70B**
- Understands user questions
- Gives safety and travel suggestions

## ⚡ Fast & Lightweight Backend
- Built using **FastAPI**
- Low latency API responses

## 🎨 Interactive Frontend
- Built with **Streamlit**
- Clean UI with background image
- Simple input form

## 🔗 API Integration
- OpenWeather API for live weather data
- Groq API for AI reasoning

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │   Streamlit UI       │
                    │  (Frontend Layer)    │
                    └─────────┬────────────┘
                              │ HTTP Request
                              ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │  (API Layer)         │
                    └─────────┬────────────┘
                              │ Weather Query
                              ▼
                    ┌──────────────────────┐
                    │ OpenWeather API      │
                    │ (Live Weather Data)  │
                    └─────────┬────────────┘
                              │ Weather Info
                              ▼
                    ┌──────────────────────┐
                    │ Groq LLM (LLaMA 3)   │
                    │ AI Reasoning Layer   │
                    └─────────┬────────────┘
                              │ Final Answer
                              ▼
                    ┌──────────────────────┐
                    │   Streamlit UI       │
                    │   JSON Output        │
                    └──────────────────────┘