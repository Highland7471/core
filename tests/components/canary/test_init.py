"""The tests for the Canary component."""
from pytest import fixture

from homeassistant.setup import setup_component
import homeassistant.components.canary as canary

from tests.async_mock import patch
from tests.common import get_test_home_assistant


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

    mock_update.assert_called_once_with()
    mock_login.assert_called_once_with()


def test_setup_with_missing_username(hass, canary) -> None:
    """Test setup with missing username."""
    config = {"canary": {"password": "bar"}}
    assert not setup_component(hass, canary.DOMAIN, config)


def test_setup_with_missing_password(hass, canary):
    """Test setup with missing password."""
    config = {"canary": {"username": "foo@bar.org"}}
    assert not setup_component(self.hass, canary.DOMAIN, config)
