"""Define fixtures available for all tests."""
from canary.api import Api
from pytest import fixture

from tests.async_mock import MagicMock, PropertyMock, patch

@fixture()
def canary(hass):
    """Mock the CanaryApi for easier testing."""
    with patch("homeassistant.components.canary.Api") as mock_canary:
        instance = mock_canary.return_value = Api(
            "test-username",
            "test-password",
            1,
        )

        instance.login = MagicMock(return_value=True)
        instance.get_entries = MagicMock(return_value=[])
        instance.get_locations = MagicMock(return_value=[])
        instance.get_location = MagicMock(return_value=None)
        instance.get_modes = MagicMock(return_value=[])
        instance.get_readings = MagicMock(return_value=[])
        instance.set_location_mode = MagicMock(return_value=None)

        yield mock_canary


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
