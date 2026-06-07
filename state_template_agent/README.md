# State Template Agent

This folder demonstrates ADK session-state templating in an agent instruction.

ADK replaces placeholders like `{user_name}` with matching values from session
state before the model receives the instruction.

## Setup

From the repo root:

```powershell
Copy-Item .\state_template_agent\.env.example .\state_template_agent\.env
```

Edit `state_template_agent\.env` and add your Google API key.

## Run

Use PowerShell-safe escaped quotes for `--state`:

```powershell
adk run state_template_agent --state '{\"user_name\":\"Maya\",\"topic\":\"Google ADK tools\",\"learning_level\":\"beginner\",\"tone\":\"friendly\"}'
```

Example prompt:

```text
Create a short study plan for me.
```

Try another personalized session:

```powershell
adk run state_template_agent --state '{\"user_name\":\"Arjun\",\"topic\":\"multi-agent routing\",\"learning_level\":\"intermediate\",\"tone\":\"direct\"}'
```

Example prompt:

```text
Explain the concept with one practical project idea.
```
