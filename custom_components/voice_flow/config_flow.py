from homeassistant import config_entries
from homeassistant.helpers.selector import ConversationAgentSelector, ConversationAgentSelectorConfig
import voluptuous as vol

DOMAIN = "voice_flow"

class VoiceFlowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the configuration flow for VoiceFlow."""

    async def async_step_user(self, user_input=None):
        """Handle the user configuration step."""
        if user_input is not None:
            return self.async_create_entry(title="VoiceFlow", data=user_input)

        # Use ConversationAgentSelector to dynamically get available agents
        data_schema = vol.Schema({
            vol.Required(
                "command_agent",
                description={"suggested_value": "assist"},
            ): ConversationAgentSelector(
                ConversationAgentSelectorConfig(language="en")
            ),
            vol.Required(
                "question_agent",
                description={"suggested_value": "assist"},
            ): ConversationAgentSelector(
                ConversationAgentSelectorConfig(language="en")
            ),
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
        )
