from google.adk.agents.llm_agent import Agent

# a simple tool the agent can call
def get_current_time(city: str) -> dict:
    """Returns the current time in a given city."""
    return {"status": "success",
            "city": city, "time": "17:35 PM"}

# a simple tool the agent can call
def get_weather(city: str) -> dict:
    """Returns the current weather in a given city."""
    return {"status": "success",
            "city": city, "weather": "sunny"}

root_agent = Agent(
    name="time_and_weather_assistant",
    model="gemini-2.5-flash",
    description="Tells the current time and weather in a city.",
    instruction="You are a helpful assistant. Use the "
                "get_current_time and get_weather tools to answer time and weather questions.",
    tools=[get_weather,get_current_time],
)
