"""The tests for the Canary component."""
from pytest import fixture

from homeassistant.setup import setup_component
import homeassistant.components.canary as canary

from tests.async_mock import MagicMock, PropertyMock, patch
from tests.common import get_test_home_assistant


@fixture
def mock_device(device_id, name, is_online=True, device_type_name=None):
    """Mock Canary Device class."""
    device = MagicMock()
    type(device).device_id = PropertyMock(return_value=device_id)
    type(device).name = PropertyMock(return_value=name)
    type(device).is_online = PropertyMock(return_value=is_online)
    type(device).device_type = PropertyMock(
        return_value={"id": 1, "name": device_type_name}
    )
    return device


@fixture
def mock_location(name, is_celsius=True, devices=None):
    """Mock Canary Location class."""
    location = MagicMock()
    type(location).name = PropertyMock(return_value=name)
    type(location).is_celsius = PropertyMock(return_value=is_celsius)
    type(location).devices = PropertyMock(return_value=devices or [])
    return location


@fixture
def mock_reading(sensor_type, sensor_value):
    """Mock Canary Reading class."""
    reading = MagicMock()
    type(reading).sensor_type = PropertyMock(return_value=sensor_type)
    type(reading).value = PropertyMock(return_value=sensor_value)
    return reading


@patch("homeassistant.components.canary.CanaryData.update")
def test_setup_with_valid_config(hass, mock_login, mock_update) -> None:
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
        assert setup_component(self.hass, canary.DOMAIN, config)

    mock_update.assert_called_once_with()
    mock_login.assert_called_once_with()


def test_setup_with_missing_username(hass) -> None:
    """Test setup with missing username."""
    config = {"canary": {"password": "bar"}}
    assert not setup_component(self.hass, canary.DOMAIN, config)

def test_setup_with_missing_password(hass):
    """Test setup with missing password."""
    config = {"canary": {"username": "foo@bar.org"}}
    assert not setup_component(self.hass, canary.DOMAIN, config)
