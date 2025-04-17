import os
import googlemaps
import pytest

@pytest.fixture
def gmaps_client(monkeypatch):
    # Mock the API key directly in the code
    monkeypatch.setenv("GOOGLE_API_KEY", "AIzaSyC2UHZ50CgCeueKLSZsp5NS7rJnUrj38gA")

    # Fetch the API key from the environment variable
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        pytest.fail("GOOGLE_API_KEY not set in environment")
    
    # Return the googlemaps client
    return googlemaps.Client(key=api_key)

def test_find_waffle_house_toledo(gmaps_client, capsys):
    # Capture the output
    response = gmaps_client.find_place(
        input="Waffle House Toledo",
        input_type="textquery",
        fields=["geometry/location", "name", "formatted_address"]
    )

    # Optionally, print the results to stdout
    candidate = response["candidates"][0]
    location = candidate["geometry"]["location"]
    print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")

    # Capture the stdout after the print statement
    captured = capsys.readouterr()

    # Assert the API response status
    assert response["status"] == "OK"
    assert "candidates" in response
    assert len(response["candidates"]) > 0
    candidate = response["candidates"][0]
    assert "geometry" in candidate
    assert "location" in candidate["geometry"]
    assert "lat" in candidate["geometry"]["location"]
    assert "lng" in candidate["geometry"]["location"]

    # Assert that the print statement was called
    assert "Latitude:" in captured.out
    assert "Longitude:" in captured.out

def test_find_waffle_house_toledo_valid(gmaps_client, capsys):
    # Valid query
    response = gmaps_client.find_place(
        input="Waffle House Toledo",
        input_type="textquery",
        fields=["geometry/location", "name", "formatted_address"]
    )
    
    # Check the response status
    assert response["status"] == "OK"
    assert "candidates" in response
    assert len(response["candidates"]) > 0
    candidate = response["candidates"][0]
    assert "geometry" in candidate
    assert "location" in candidate["geometry"]
    assert "lat" in candidate["geometry"]["location"]
    assert "lng" in candidate["geometry"]["location"]
    
    # Capture the stdout before assertions
    captured = capsys.readouterr()
    
    # Ensure latitude and longitude are printed
    location = candidate["geometry"]["location"]
    print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")

    # Capture again after print
    captured = capsys.readouterr()

    # Assert that the print statement was called
    assert "Latitude:" in captured.out
    assert "Longitude:" in captured.out


def test_find_invalid_input(gmaps_client):
    # Invalid input (empty string)
    try:
        response = gmaps_client.find_place(
            input="",
            input_type="textquery",
            fields=["geometry/location", "name", "formatted_address"]
        )
    except googlemaps.exceptions.ApiError as e:
        # Assert the exception was raised
        assert str(e) == 'INVALID_REQUEST'




def test_missing_expected_fields(gmaps_client):
    # Query that may not return expected fields
    response = gmaps_client.find_place(
        input="Waffle House Toledo",
        input_type="textquery",
        fields=["geometry/location", "name"]  # Notice "formatted_address" is missing
    )

    # Assert the response contains the expected fields
    assert response["status"] == "OK"
    assert "candidates" in response
    candidate = response["candidates"][0]
    assert "name" in candidate
    assert "geometry" in candidate
    assert "location" in candidate["geometry"]
    assert "lat" in candidate["geometry"]["location"]
    assert "lng" in candidate["geometry"]["location"]


def test_specific_location_coordinates(gmaps_client):
    # Query for a specific place
    response = gmaps_client.find_place(
        input="Waffle House Toledo",
        input_type="textquery",
        fields=["geometry/location", "name", "formatted_address"]
    )

    # Expected latitude and longitude for Waffle House Toledo
    expected_lat = 41.5950663
    expected_lng = -83.6653049

    candidate = response["candidates"][0]
    location = candidate["geometry"]["location"]

    assert location['lat'] == expected_lat
    assert location['lng'] == expected_lng


