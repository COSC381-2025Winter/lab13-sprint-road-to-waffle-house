from googlemaps import convert 
import googlemaps
from road_to_waffle_house.where_is_waffle_house import *

done = False

def getUserAddress():
    #### RYAN
    # prompts user for location you are at
    return input("Enter to your location: ")

def run(user_input):
    global done
    api_key = "AIzaSyC2UHZ50CgCeueKLSZsp5NS7rJnUrj38gA"
    
    ## We can pass origins in this format or via coordinates, 
    yourLocation = user_input

    # Define your origins and destinations
    origins_coords = [yourLocation]

    try:
        destinations_coords = [get_waffle_house_location(yourLocation).get("formatted_address")]  # (closest waffle house)

    except:
        done = False
        return
    
    """
    Calculate the distance matrix by calling the function.
    Since we have everything but API key, origins and destinations, everting else can use default values
    """
    distance_matrix_result = calculate_distance_matrix(
        api_key=api_key,
        origins=origins_coords,
        destinations=destinations_coords,
    )

    # Print the results
    if distance_matrix_result:
        print("Distance Matrix Results:")
        for i, row in enumerate(distance_matrix_result['rows']):
            for j, element in enumerate(row['elements']):
                origin = origins_coords[i]
                destination = destinations_coords[j]
                status = element['status']
                distance = element['distance']['text']
                duration = element['duration']['text']
                print(f"From {origin} to {destination}:")
                print(f"  Distance: {distance}")
                print(f"  Duration: {duration}")
                done = True
                return (distance, duration)
                 
# Gets travel distance and time for a matrix of origins and destinations.
def calculate_distance_matrix(api_key, origins, destinations, mode=None,
                              language=None, avoid=None, units="imperial",
                              departure_time=None, arrival_time=None, transit_mode=None,
                              transit_routing_preference=None, traffic_model=None, region=None):
    """
    Just documentation from the repo that we can use. it states all parameters above, 
    we can change them as needed.

    Gets travel distance and time for a matrix of origins and destinations.

    { :param origins: One or more addresses, Place IDs, and/or latitude/longitude
        values, from which to calculate distance and time. Each Place ID string
        must be prepended with 'place_id:'. If you pass an address as a string,
        the service will geocode the string and convert it to a
        latitude/longitude coordinate to calculate directions.
        
    :type origins: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple   }

    { :param destinations: One or more addresses, Place IDs, and/or lat/lng values,
        to which to calculate distance and time. Each Place ID string must be
        prepended with 'place_id:'. If you pass an address as a string, the
        service will geocode the string and convert it to a latitude/longitude
        coordinate to calculate directions.
        
    :type destinations: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple }

    { :param mode: Specifies the mode of transport to use when calculating
        directions. Valid values are "driving", "walking", "transit" or
        "bicycling".
        
    :type mode: string }

    { :param language: The language in which to return results.
    :type language: string }

    { :param avoid: Indicates that the calculated route(s) should avoid the
        indicated features. Valid values are "tolls", "highways" or "ferries".
    :type avoid: string }

    { :param units: Specifies the unit system to use when displaying results.
        Valid values are "metric" or "imperial".
    :type units: string }

    { :param departure_time: Specifies the desired time of departure.
    :type departure_time: int or datetime.datetime }

    { :param arrival_time: Specifies the desired time of arrival for transit
        directions. Note: you can't specify both departure_time and
        arrival_time.
    :type arrival_time: int or datetime.datetime }

    { :param transit_mode: Specifies one or more preferred modes of transit.
        This parameter may only be specified for requests where the mode is
        transit. Valid values are "bus", "subway", "train", "tram", "rail".
        "rail" is equivalent to ["train", "tram", "subway"].
    :type transit_mode: string or list of strings }

    { :param transit_routing_preference: Specifies preferences for transit
        requests. Valid values are "less_walking" or "fewer_transfers".
    :type transit_routing_preference: string }

    :param traffic_model: Specifies the predictive travel time model to use.
        Valid values are "best_guess" or "optimistic" or "pessimistic".
        The traffic_model parameter may only be specified for requests where
        the travel mode is driving, and where the request includes a
        departure_time.

    { :param region: Specifies the preferred region the geocoder should search
        first, but it will not restrict the results to only this region. Valid
        values are a ccTLD code.
    :type region: string }

    :rtype: matrix of distances. Results are returned in rows, each row
        containing one origin paired with each destination.
    """
    try:
        gmaps = googlemaps.Client(key=api_key)
        result = gmaps.distance_matrix(
            origins=origins,
            destinations=destinations,
            mode=mode,
            avoid=avoid,
            units=units,
            language=language,
            region=region,
            departure_time=departure_time,
            arrival_time=arrival_time,
            transit_mode=transit_mode,
            traffic_model=traffic_model,
            transit_routing_preference=transit_routing_preference
        )
        # error handling 
        print("API successfully executed ")
        return result
  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
