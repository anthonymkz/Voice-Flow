from __future__ import annotations

import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.components.conversation import (
    AbstractConversationAgent,
    ConversationInput,
    ConversationResult,
)

_LOGGER = logging.getLogger(__name__)

class VoiceFlowConversationAgent(AbstractConversationAgent):
    """VoiceFlow conversation agent."""

    def __init__(self, hass: HomeAssistant, smarthome_agent: str, general_agent: str, location_sensor: str | None = None) -> None:
        """Initialize the VoiceFlow agent."""
        self.hass = hass
        self.command_agent = command_agent
        self.question_agent = question_agent
        self.id = "voice_flow"
        self.name = "VoiceFlow"

    async def async_process(self, input: ConversationInput) -> ConversationResult:
        """Process a conversation input."""
        text = input.text.strip().lower()

        _LOGGER.debug("Received text: '%s'", text)

        # Determine the target agent based on the first keyword
        if text.startswith("command"):
            query = text[len("command"):].strip()
            target_agent = self.smarthome_agent
        elif text.startswith("question"):
            query = text[len("question"):].strip()
            target_agent = self.general_agent
        else:
            # Let Home Assistant handle unmatched queries with the default agent
            query = text
            target_agent = None  # No specific agent
            include_location = False

        _LOGGER.debug("Routing to agent: %s with query: %s", target_agent or 'default', query)

        # Build action data payload
        action_data = {
            "text": query,
            "language": input.language,
        }
        if target_agent:
            action_data["agent_id"] = target_agent
        if input.conversation_id:
            action_data["conversation_id"] = input.conversation_id

        try:
            # Execute the action for conversation.process
            response = await self.hass.services.async_call(
                "conversation",
                "process",
                action_data,
                blocking=True,
                return_response=True,
            )

            # Extract response text
            speech_response = response.get("response", {}).get("speech", {}).get("plain", {}).get("speech", "Sorry, I couldn't process your request.")
        except Exception as err:
            _LOGGER.error("Error during action execution: %s", err)
            speech_response = "An error occurred while processing your request."

        # Return the result
        return ConversationResult(
            response=speech_response,
            conversation_id=input.conversation_id,
            language=input.language,
        )
