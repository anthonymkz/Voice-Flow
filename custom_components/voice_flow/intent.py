from homeassistant.helpers import intent
from homeassistant.core import HomeAssistant
from homeassistant.helpers.intent import IntentResponse
from homeassistant.config_entries import ConfigEntry

class VoiceFlowCommandIntentHandler(intent.IntentHandler):
    """Handle smart home commands."""

    intent_type = "VoiceFlowCommand"

    def __init__(self, hass: HomeAssistant, command_agent: str):
        """Initialize with Home Assistant instance and smart home agent."""
        self.hass = hass
        self.command_agent = command_agent

    async def async_handle(self, intent_obj: intent.Intent) -> IntentResponse:
        """Handle the intent for smart home commands."""
        query = intent_obj.slots.get("query", {}).get("value", "")

        if not query:
            response = IntentResponse(language="en")
            response.async_set_speech("No command text was provided.")
            return response

        result = await self.hass.services.async_call(
            "conversation",
            "process",
            {
                "text": query,
                "agent_id": self.command_agent,
            },
            blocking=True,
            return_response=True,
        )

        speech_response = result.get("response", {}).get("speech", {}).get("plain", {}).get("speech", "Command processed.")

        response = IntentResponse(language="en")
        response.async_set_speech(speech_response)
        return response


class VoiceFlowQuestionIntentHandler(intent.IntentHandler):
    """Handle general inquiries."""

    intent_type = "VoiceFlowQuestion"

    def __init__(self, hass: HomeAssistant, question_agent: str):
        """Initialize with Home Assistant instance and general inquiry agent."""
        self.hass = hass
        self.question_agent = question_agent

    async def async_handle(self, intent_obj: intent.Intent) -> IntentResponse:
        """Handle the intent for general inquiries."""
        query = intent_obj.slots.get("query", {}).get("value", "")

        if not query:
            response = IntentResponse(language="en")
            response.async_set_speech("No question text was provided.")
            return response

        result = await self.hass.services.async_call(
            "conversation",
            "process",
            {
                "text": query,
                "agent_id": self.question_agent,
            },
            blocking=True,
            return_response=True,
        )

        speech_response = result.get("response", {}).get("speech", {}).get("plain", {}).get("speech", "Query processed.")

        response = IntentResponse(language="en")
        response.async_set_speech(speech_response)
        return response


async def async_get_config_entry(hass: HomeAssistant) -> ConfigEntry | None:
    """Get the config entry for the VoiceFlow integration."""
    from . import DOMAIN
    entries = hass.config_entries.async_entries(DOMAIN)
    return entries[0] if entries else None


async def async_setup_intents(hass: HomeAssistant) -> None:
    """Set up the VoiceFlow intents."""
    config_entry = await async_get_config_entry(hass)
    if not config_entry:
        return

    command_agent = config_entry.data["command_agent"]
    question_agent = config_entry.data["question_agent"]

    hass.helpers.intent.async_register(
        VoiceFlowCommandIntentHandler(hass, command_agent)
    )
    hass.helpers.intent.async_register(
        VoiceFlowQuestionIntentHandler(hass, question_agent)
    )