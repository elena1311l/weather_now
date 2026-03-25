import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_KEY)

def get_advice (weather_data):
    try:
        model= genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Based on the weather details: {weather_data}, provide appropriate advice."
        response = model.generate_content(prompt)
        if response and response.text:
            return response.text
        return "AI did not return any advice."
    except Exception as e:
        return f"Error: {e}"