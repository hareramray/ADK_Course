from google.adk.agents import Agent


root_agent = Agent(
    name="state_template_assistant",
    model="gemini-2.5-flash",
    description="Demonstrates ADK instruction personalization with session state.",
    instruction=(
        "You are a personal learning assistant for {user_name}.\n"
        "The user's current topic is {topic}.\n"
        "Their learning level is {learning_level}.\n"
        "Use a {tone} tone.\n\n"
        "When answering, greet {user_name} by name, keep examples focused on "
        "{topic}, and adjust the depth for a {learning_level} learner."
    ),
)
