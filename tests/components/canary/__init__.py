"""Tests for the canary component."""
from tests.async_mock import MagicMock, PropertyMock


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


def mock_location(name, is_celsius=True, devices=None):
    """Mock Canary Location class."""
    location = MagicMock()
    type(location).name = PropertyMock(return_value=name)
    type(location).is_celsius = PropertyMock(return_value=is_celsius)
    type(location).devices = PropertyMock(return_value=devices or [])
    return location


def mock_reading(sensor_type, sensor_value):
    """Mock Canary Reading class."""
    reading = MagicMock()
    type(reading).sensor_type = PropertyMock(return_value=sensor_type)
    type(reading).value = PropertyMock(return_value=sensor_value)
    return reading
