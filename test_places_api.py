import pytest
from unittest.mock import patch
from where_is_waffle_house import get_waffle_house_location
import googlemaps  


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


@patch("where_is_waffle_house.googlemaps.Client")
def test_find_invalid_input(mock_client_class):
    mock_client = mock_client_class.return_value

    mock_client.geocode.return_value = [{
        "geometry": {
            "location": {
                "lat": 41.5950663,
                "lng": -83.6653049
            }
        }
    }]

    mock_client.places.return_value = {
        "status": "INVALID_REQUEST",
        "results": []
    }

    from where_is_waffle_house import get_waffle_house_location
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


@patch("where_is_waffle_house.googlemaps.Client")
def test_specific_location_coordinates(mock_client_class):
    expected_lat = 41.5950663
    expected_lng = -83.6653049

    mock_client = mock_client_class.return_value

    mock_client.geocode.return_value = [{
        "geometry": {
            "location": {
                "lat": expected_lat,
                "lng": expected_lng
            }
        }
    }]

    mock_client.places.return_value = {
        "results": [
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

    from where_is_waffle_house import get_waffle_house_location
    result = get_waffle_house_location("123 Waffle St, Toledo, OH")
    location = result["geometry"]["location"]

    assert location["lat"] == expected_lat
    assert location["lng"] == expected_lng

# Timeout Error
@patch("where_is_waffle_house.googlemaps.Client.geocode")
def test_timeout_error(mock_geocode, capsys):
    mock_geocode.side_effect = googlemaps.exceptions.Timeout("Request timed out")
    result = get_waffle_house_location("123 Waffle St, Toledo, OH")
    captured = capsys.readouterr()
    assert result is None
    assert "Request timed out" in captured.out

# API Error
@patch("where_is_waffle_house.googlemaps.Client.geocode")
def test_api_error(mock_geocode, capsys):
    mock_geocode.side_effect = googlemaps.exceptions.ApiError("API error occurred", "status")
    result = get_waffle_house_location("123 Waffle St, Toledo, OH")
    captured = capsys.readouterr()
    assert result is None
    assert "API error occurred" in captured.out

# Generic Exception
@patch("where_is_waffle_house.googlemaps.Client.geocode")
def test_generic_error(mock_geocode, capsys):
    mock_geocode.side_effect = Exception("An unexpected error occurred")
    result = get_waffle_house_location("123 Waffle St, Toledo, OH")
    captured = capsys.readouterr()
    assert result is None
    assert "An unexpected error occurred" in captured.out

@patch("where_is_waffle_house.googlemaps.Client.places")
def test_empty_results(mock_places, capsys):
    # Simulate the API response with 'results' being an empty list
    mock_places.return_value = {
        'results': []  # 'results' is an empty list
    }

    # Call the function with a test address
    result = get_waffle_house_location("123 Waffle St, Toledo, OH")

    # Capture printed output using capsys
    captured = capsys.readouterr()

    # Assert that the function returns None when no Waffle House is found
    assert result is None

    # Assert that the printed output contains the expected message
    assert "No Waffle House found near: 123 Waffle St, Toledo, OH" in captured.out

@patch("where_is_waffle_house.googlemaps.Client.places")
def test_no_results_field(mock_places, capsys):
    # Simulate the API response with no 'results' field at all
    mock_places.return_value = {}  # No 'results' in response

    # Call the function with a test address
    result = get_waffle_house_location("123 Waffle St, Toledo, OH")

    # Capture printed output using capsys
    captured = capsys.readouterr()

    # Assert that the function returns None when no Waffle House is found
    assert result is None

    # Assert that the printed output contains the expected message
    assert "No Waffle House found near: 123 Waffle St, Toledo, OH" in captured.out
