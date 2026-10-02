"""Constants for the Mold Guard integration."""

DOMAIN = "mold_guard"

# Standard-Schwellenwerte für Schimmelschutz bei 18-20 °C Raumtemperatur
DEFAULT_ABSOLUTE_HUMIDITY_THRESHOLD = 8.5  # g/m³ (entspricht ~55% rF bei 18 °C)
DEFAULT_HUMIDITY_DIFF = 1.5                # g/m³ (Mindestdifferenz nach draußen)
DEFAULT_TEMP_MIN = 18.5                    # °C Untergrenze für Kältewarnung
DEFAULT_WINDOW_TIMEOUT = 10                # Minuten bis zur Schließ-Erinnerung
