import googlemaps
import os

import googlemaps

def get_waffle_house_location(address):
    api_key = "AIzaSyC2UHZ50CgCeueKLSZsp5NS7rJnUrj38gA"  
    gmaps = googlemaps.Client(key=api_key)

    try:
        # Geocode the address to get latitude and longitude
        geocode_result = gmaps.geocode(address)
        if not geocode_result:
            print(f"Geocoding failed for address: {address}")
            return None

        location = geocode_result[0]["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]

        # Search for Waffle House locations near the specified location
        response = gmaps.places(
            query="Waffle House",
            location=(latitude, longitude),
            radius=5000000,  # 50 km radius
            type="restaurant"
        )

        # Check if response contains results and iterate through them
        if 'results' not in response or not response['results']:
            print(f"No Waffle House found near: {address}")
            return None

        # Iterate through results to find an exact match for Waffle House
        for place in response['results']:
            if place['name'].lower() == "waffle house":
                return place

        #print(f"No official Waffle House found near: {address}")
        #return None

    except googlemaps.exceptions.Timeout as e:
        print(f"Request timed out: {str(e)}")  # Use str() to convert the exception message to string
        return None
    except googlemaps.exceptions.ApiError as e:
        print(f"API error occurred: {str(e)}")  # Use str() to convert the exception message to string
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")  # Use str() to convert the exception message to string
        return None


