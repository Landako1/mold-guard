"""Config flow for Mold Guard integration."""
import voluptuous as vol
from homeassistant import config_entries
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, DEFAULT_ABSOLUTE_HUMIDITY_THRESHOLD, DEFAULT_HUMIDITY_DIFF

class MoldGuardConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handhabt den Konfigurations-Ablauf in der HA Benutzeroberfläche."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=user_input["room_name"], data=user_input)

        data_schema = vol.Schema({
            vol.Required("room_name", default="Wohnzimmer"): str,
            vol.Required("temp_sensor"): cv.entity_id,
            vol.Required("humidity_sensor"): cv.entity_id,
            vol.Required("outdoor_temp_sensor"): cv.entity_id,
            vol.Required("outdoor_humidity_sensor"): cv.entity_id,
            vol.Optional("window_contact"): cv.entity_id,
            vol.Optional("notify_service", default="notify.alle_handys"): str,
            vol.Optional("abs_humidity_threshold", default=DEFAULT_ABSOLUTE_HUMIDITY_THRESHOLD): float,
            vol.Optional("humidity_diff", default=DEFAULT_HUMIDITY_DIFF): float,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
