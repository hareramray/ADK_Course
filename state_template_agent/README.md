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

## Run In The Web UI

Start the ADK web UI from the repo root:

```powershell
adk web .
```

Open the local URL that ADK prints, then select `state_template_agent`.

Use this prompt to save state from the web UI:

```text
Save my profile: my name is Hareram, my topic is Google ADK tools, my learning level is beginner, and my preferred tone is friendly.
```

Then ask a follow-up in the same session:

```text
Create a short study plan for me.
```

The first message calls the `save_profile` tool and writes values into session
state. The next message shows `{user_name}`, `{topic}`, `{learning_level}`, and
`{tone}` being used from the saved session state.

By default, `adk web` stores sessions under local `.adk` storage. Avoid
`--no_use_local_storage` or `--session_service_uri memory://` if you want the
saved state to survive server restarts.
