from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def save_profile(
    user_name: str,
    topic: str,
    learning_level: str,
    tone: str,
    tool_context: ToolContext,
) -> dict:
    """Saves personalization values into session state."""
    profile = {
        "user_name": user_name,
        "topic": topic,
        "learning_level": learning_level,
        "tone": tone,
    }
    tool_context.state.update(profile)
    return {
        "status": "success",
        "saved_profile": profile,
    }


root_agent = Agent(
    name="state_template_assistant",
    model="gemini-2.5-flash",
    description="Demonstrates ADK instruction personalization with session state.",
    instruction=(
        "You are a personal learning assistant.\n\n"
        "Saved session profile:\n"
        "- user_name: {user_name?}\n"
        "- topic: {topic?}\n"
        "- learning_level: {learning_level?}\n"
        "- tone: {tone?}\n\n"
        "If the user asks to save or update their profile, call save_profile.\n"
        "If profile details are missing, ask for them briefly.\n"
        "When profile details are available, greet the user by name, keep "
        "examples focused on their topic, match their learning level, and use "
        "their preferred tone."
    ),
    tools=[save_profile],
)
