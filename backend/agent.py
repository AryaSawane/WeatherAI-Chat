import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate

# Simple weather function (no API needed for now)
def get_weather(city: str) -> str:
    """REAL weather from OpenWeatherMap API"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key or len(api_key) < 20:
        return f"Weather in {city}: Get API key from openweathermap.org"
    
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        import requests
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"{desc.capitalize()}, {temp}°C in {city}"
        return f"City '{city}' not found"
    except:
        return f"Weather service unavailable"


load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0,
)

@tool
def weather_tool(city: str) -> str:
    """Get the current weather of a city."""
    return get_weather(city)

llm_with_tools = llm.bind_tools([weather_tool])

prompt = ChatPromptTemplate.from_template(
    "You are a weather assistant. Use the weather tool for weather questions.\n\nQuestion: {input}\nAnswer:"
)

chain = prompt | llm_with_tools

async def invoke_agent(input_text: str):
    try:
        result = await chain.ainvoke({"input": input_text})
        
        # Handle tool calls manually
        if hasattr(result, 'tool_calls') and result.tool_calls:
            tool_call = result.tool_calls[0]
            if tool_call['name'] == 'weather_tool':
                tool_result = weather_tool.invoke(tool_call['args'])
                return tool_result  # Direct return for simplicity
        
        return result.content or "No response"
    except Exception as e:
        return f"Error: {str(e)}"
