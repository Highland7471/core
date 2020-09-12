"""The tests for the Canary component."""
from homeassistant.setup import setup_component
import homeassistant.components.canary as canary

from tests.async_mock import patch


def test_setup_with_valid_config(hass, canary) -> None:
    """Test setup with valid YAML."""
    config = {"canary": {"username": "foo@bar.org", "password": "bar"}}

    with patch(
        "homeassistant.components.canary.alarm_control_panel.setup_platform",
        return_value=True,
    ), patch(
        "homeassistant.components.canary.camera.setup_platform",
        return_value=True,
    ), patch(
        "homeassistant.components.canary.sensor.setup_platform",
        return_value=True,
    ):
        assert setup_component(hass, canary.DOMAIN, config)
