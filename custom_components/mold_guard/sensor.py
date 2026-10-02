"""Sensor platform for Mold Guard."""
import math
import logging
from homeassistant.components.sensor import SensorEntity, SensorStateClass

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

def calculate_absolute_humidity(temperature: float, humidity: float) -> float:
    """Berechnet die absolute Feuchte in g/m³ nach der Magnus-Formel."""
    if temperature is None or humidity is None:
        return 0.0
    
    # Sättigungsdampfdruck in hPa
    if temperature >= 0:
        a, b = 7.5, 237.3
    else:
        a, b = 9.5, 265.5
        
    sdd = 6.1078 * (10 ** ((a * temperature) / (b + temperature)))
    dd = sdd * (humidity / 100.0)
    af = (216.7 * dd) / (273.15 + temperature)
    return round(af, 2)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Mold Guard sensors."""
    config = entry.data
    room_name = config.get("room_name")
    
    async_add_entities([
        AbsoluteHumiditySensor(
            hass,
            f"{room_name} Absolute Feuchte",
            config.get("temp_sensor"),
            config.get("humidity_sensor"),
            f"mold_guard_{entry.entry_id}_abs_humidity"
        )
    ])


class AbsoluteHumiditySensor(SensorEntity):
    """Sensor zur Darstellung der absoluten Feuchte in g/m³."""

    def __init__(self, hass, name, temp_entity, humidity_entity, unique_id):
        self.hass = hass
        self._name = name
        self._temp_entity = temp_entity
        self._humidity_entity = humidity_entity
        self._unique_id = unique_id
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def native_value(self):
        return self._state

    @property
    def native_unit_of_measurement(self):
        return "g/m³"

    @property
    def state_class(self):
        return SensorStateClass.MEASUREMENT

    @property
    def icon(self):
        return "mdi:water-percent"

    def update(self):
        """Holt die aktuellen Werte und berechnet die absolute Feuchte."""
        temp_state = self.hass.states.get(self._temp_entity)
        hum_state = self.hass.states.get(self._humidity_entity)

        if temp_state and hum_state and temp_state.state not in ("unavailable", "unknown") and hum_state.state not in ("unavailable", "unknown"):
            try:
                temp = float(temp_state.state)
                hum = float(hum_state.state)
                self._state = calculate_absolute_humidity(temp, hum)
            except ValueError:
                self._state = None
