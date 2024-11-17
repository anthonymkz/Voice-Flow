# VoiceFlow Integration

![VoiceFlow Integration Overview](https://via.placeholder.com/1000x400?text=Integration+Image+Placeholder)

VoiceFlow Integration is a powerful Home Assistant add-on that enables seamless routing of user commands and queries to specified agents. Simplify your smart home interactions with categorized inputs and tailored responses.

[![Stars](https://img.shields.io/github/stars/anthonymkz/voice-flow)](https://github.com/anthonymkz/voice-flow) [![Last commit](https://img.shields.io/github/last-commit/anthonymkz/voice-flow)](https://github.com/anthonymkz/voice-flow) [![Home Assistant Community Forum](https://img.shields.io/badge/Home%20Assistant-Community%20Forum-blue?logo=home-assistant)](https://community.home-assistant.io/) [![Buy me a coffee](https://img.shields.io/badge/Donate-Buy%20me%20a%20coffee-yellow?logo=buy-me-a-coffee)](https://buymeacoffee.com/anthonymkz)

<br>

## Table of Contents

**[`Overview`](#overview)**  **[`Features`](#features)**  **[`Installation`](#installation)**  **[`Configuration`](#configuration)**  **[`Usage`](#usage)**  **[`Suggested Prompt`](#suggested-prompt)**  **[`Contributing`](#contributing)**  **[`Donate`](#donate)**  **[`Planned Features`](#planned-features)**  **[`Notes`](#notes)**

<br>

## Overview

VoiceFlow Integration routes user commands and questions to specific agents in Home Assistant. It uses two interaction types:
- **Command:** Directed to smart home agents (e.g., "Turn on the lights").
- **Question:** Directed to general inquiry agents (e.g., "What’s the weather tomorrow?").

This design streamlines smart home actions and query handling.

---

## Features

- **Dynamic Agent Routing:** Handle inputs seamlessly based on context.
- **Customizable Behavior:** Tailor the integration for unique smart home and inquiry needs.
- **Lightweight Setup:** Minimal configuration requirements.

---

## Installation

### Manual Installation

1. **Download and Place Files:**
   - Download the repository and copy the `voice_flow` folder into your Home Assistant `custom_components` directory.
     - Path: `config/custom_components/voice_flow/`

2. **Create Custom Sentences Directory:**
   - If the directory doesn’t exist, create it:
     - Path: `config/custom_sentences/en/`

3. **Add Sentences File:**
   - Create a file in `custom_sentences/en/`:
     - File name: `voiceflow.yaml`
     - Copy the contents found [HERE](https://gist.github.com/anthonymkz/c9bbe4899edaff9983a1ad0fc0761e74).

4. **Restart Home Assistant:**
   - Restart to apply changes.

---

## Configuration

1. Go to **Settings > Devices & Services**.
2. Click **+ Add Integration** and search for `VoiceFlow`.
3. Follow the prompts to configure the following:
   - Assign an agent for `question` inputs, such as a local or cloud-based AI.
   - Assign an agent for `command` inputs. By default, commands without a keyword will route to `Home Assistant Assist`. However, you can use the `command` keyword to direct specific inputs to a different agent for additional functionality or leave it as Assist to ensure certain commands route to Home Assistant.
4. Save changes. Your integration is now ready.

---

## Usage

- **Command Inputs:**
  - Commands without a keyword will route to Home Assistant Assist by default.
  - Use the `command` keyword to direct specific commands to another agent if desired.
  - Example: `Command turn on the kitchen lights`.

- **Question Inputs:**
  - Use the `question` keyword to direct general inquiries to your chosen agent (e.g., a local or cloud-based AI).
  - Example: `Question what’s the weather tomorrow?`.

---

## Suggested Prompt

To personalize your agents and ensure a smooth user experience, we recommend using the following prompt as a starting point. Assigning a name to your agent allows users to confirm which agent they’re interacting with by keyword. Feel free to adjust the prompt or change the name to suit your needs:

> **Prompt:**  
> "You are Jarvis, a conversational assistant. Your role is to respond thoughtfully and efficiently to user inputs. Provide concise, helpful, and friendly answers tailored to the user's needs."

This prompt is entirely customizable, and you’re encouraged to modify it to better fit your specific use case or preferences.

---

## Contributing

We welcome contributions! Whether you’re fixing bugs, improving documentation, or adding features, your help is valued. Visit our [GitHub repository](https://github.com/anthonymkz/voice-flow) to get started.

---

## Donate

If you find this integration helpful, consider supporting its development:

[![Buy me a coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://buymeacoffee.com/anthonymkz){:width="200px"}

---

## Planned Features

- User-defined custom command keywords.
- Enhanced logging for improved debugging.
- Expanded agent integration.

---

## Notes

- Ensure the `voiceflow.yaml` file is created in `config/custom_sentences/en/` Contents found [HERE](https://gist.github.com/anthonymkz/c9bbe4899edaff9983a1ad0fc0761e74).
- This integration is currently for manual installation and is awaiting HACS approval.
