import googlemaps

# Initialize client with your API key
gmaps = googlemaps.Client(key="AIzaSyC2UHZ50CgCeueKLSZsp5NS7rJnUrj38gA")

# Search for the place
response = gmaps.find_place(
    input="Waffle House Toledo",
    input_type="textquery",
    fields=["geometry/location", "name", "formatted_address"]
)

# Extract and print latitude and longitude
if response["status"] == "OK" and response["candidates"]:
    place = response["candidates"][0]
    location = place["geometry"]["location"]
    print(f"Name: {place['name']}")
    print(f"Address: {place['formatted_address']}")
    print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")
else:
    print("No results found.")
