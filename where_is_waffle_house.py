import googlemaps
import os


def get_waffle_house_location():
    api_key = "AIzaSyC2UHZ50CgCeueKLSZsp5NS7rJnUrj38gA"
    gmaps = googlemaps.Client(api_key)
    response = gmaps.find_place(
        input="Waffle House Toledo",
        input_type="textquery",
        fields=["geometry/location", "name", "formatted_address"]
    )
    if response["status"] == "OK" and response["candidates"]:
        return response["candidates"][0]
    return None
