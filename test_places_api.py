import pytest
from unittest.mock import patch
from where_is_waffle_house import get_waffle_house_location


@patch("where_is_waffle_house.googlemaps.Client.find_place")
def test_find_waffle_house_toledo(mock_find_place, capsys):
    mock_find_place.return_value = {
        "status": "OK",
        "candidates": [
            {
                "name": "Waffle House",
                "formatted_address": "123 Waffle St, Toledo, OH",
                "geometry": {
                    "location": {
                        "lat": 41.5950663,
                        "lng": -83.6653049
                    }
                }
            }
        ]
    }

    result = get_waffle_house_location("123 Waffle St, Toledo, OH")

    assert result is not None
    location = result["geometry"]["location"]
    print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")

    captured = capsys.readouterr()
    assert "Latitude:" in captured.out
    assert "Longitude:" in captured.out


@patch("where_is_waffle_house.googlemaps.Client.find_place")
def test_find_waffle_house_toledo_valid(mock_find_place, capsys):
    mock_find_place.return_value = {
        "status": "OK",
        "candidates": [
            {
                "name": "Waffle House",
                "formatted_address": "456 Pancake Blvd, Toledo, OH",
                "geometry": {
                    "location": {
                        "lat": 41.5950663,
                        "lng": -83.6653049
                    }
                }
            }
        ]
    }

    result = get_waffle_house_location("123 Waffle St, Toledo, OH")
    assert result is not None
    location = result["geometry"]["location"]
    print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")

    captured = capsys.readouterr()
    assert "Latitude:" in captured.out
    assert "Longitude:" in captured.out


@patch("where_is_waffle_house.googlemaps.Client.find_place")
def test_find_invalid_input(mock_find_place):
    # Simulate API returning an error status
    mock_find_place.return_value = {
        "status": "INVALID_REQUEST",
        "candidates": []
    }

    result = get_waffle_house_location("123 Waffle St, Toledo, OH")
    assert result is None


@patch("where_is_waffle_house.googlemaps.Client.find_place")
def test_missing_expected_fields(mock_find_place):
    # Simulate API response missing formatted_address
    mock_find_place.return_value = {
        "status": "OK",
        "candidates": [
            {
                "name": "Waffle House",
                "geometry": {
                    "location": {
                        "lat": 41.5950663,
                        "lng": -83.6653049
                    }
                }
            }
        ]
    }

    result = get_waffle_house_location("123 Waffle St, Toledo, OH")
    assert result is not None
    assert "name" in result
    assert "geometry" in result
    assert "location" in result["geometry"]
    assert "lat" in result["geometry"]["location"]
    assert "lng" in result["geometry"]["location"]


@patch("where_is_waffle_house.googlemaps.Client.find_place")
def test_specific_location_coordinates(mock_find_place):
    expected_lat = 41.5950663
    expected_lng = -83.6653049

    mock_find_place.return_value = {
        "status": "OK",
        "candidates": [
            {
                "name": "Waffle House",
                "formatted_address": "789 Syrup Ave, Toledo, OH",
                "geometry": {
                    "location": {
                        "lat": expected_lat,
                        "lng": expected_lng
                    }
                }
            }
        ]
    }

    result = get_waffle_house_location("123 Waffle St, Toledo, OH")
    location = result["geometry"]["location"]

    assert location["lat"] == expected_lat
    assert location["lng"] == expected_lng
