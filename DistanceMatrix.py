from googlemaps import convert
import googlemaps
import os

def calculate_distance_matrix(api_key, origins, destinations,mode=None, language=None, avoid=None, units=None,
                    departure_time=None, arrival_time=None, transit_mode=None,
                    transit_routing_preference=None, traffic_model=None, region=None):
    """
    Calculates the distance and duration between multiple origins and destinations using the Google Distance Matrix API.

    Args:
        api_key (str): Your Google Maps Platform API key.
        origins (list of str or tuples): One or more locations to travel from. Specify as strings (addresses or place IDs)
                                         or as (latitude, longitude) tuples.
        destinations (list of str or tuples): One or more destination locations. Specify as strings (addresses or place IDs)
                                            or as (latitude, longitude) tuples.
        mode (str, optional): The travel mode to use when calculating directions.
                             Valid values are "driving", "walking", "bicycling", or "transit". Defaults to None (driving).
        transit_options (dict, optional): Specifies options that are only valid for transit requests. See Google Maps API documentation for details.
        avoid (str or list of str, optional): Restrictions to place on the request. Valid values are:
                                              "tolls", "highways", "ferries", "indoor". Defaults to None.
        units (str, optional): Specifies the unit system to use when displaying results.
                              Valid values are "metric" or "imperial". Defaults to None (API default).
        language (str, optional): The language in which to return results. See Google Maps API documentation for supported languages.
        region (str, optional): The region code, specified as a ccTLD ("top-level domain") two-character value.
        departure_time (datetime or int, optional): Specifies the desired time of departure as a datetime object or seconds since midnight, January 1, 1970 UTC.
        arrival_time (datetime or int, optional): Specifies the desired time of arrival for transit requests as a datetime object or seconds since midnight, January 1, 1970 UTC.
        travel_mode (str, optional): Specifies the mode of transport to use in transit requests. Valid values are "bus", "rail", "subway", "train", "tram".
        driving_options (dict, optional): Specifies options that are only valid for driving requests. See Google Maps API documentation for details.
        traffic_model (str, optional): Specifies the assumptions to use when calculating time in traffic. Valid values are "best_guess", "pessimistic", "optimistic". Only applicable when `mode` is "driving" and `departure_time` is specified.
        optimize_waypoint_order (bool, optional): If set to True, the Directions service will attempt to re-order the supplied waypoints to minimize the overall cost of the route. Only applicable when there is more than one waypoint. Defaults to False.

    Returns:
        dict: A dictionary representing the JSON response from the Distance Matrix API.
              Returns None if an error occurs.
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
           # travel_mode=travel_mode, was fucking up code 
            transit_mode = transit_mode,
            traffic_model=traffic_model,
           transit_routing_preference= transit_routing_preference
        )
        return result
    except googlemaps.exceptions.ApiError as e:
        print(f"An API error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
if __name__ == "__main__":
    # Replace with your actual Google Maps Platform API key
   # api_key = os.environ.get("GOOGLE_MAPS_API_KEY") #WHAT THE FUCK IS THAT
    api_key = "AIzaSyC2UHZ50CgCeueKLSZsp5NS7rJnUrj38gA"
    if not api_key:
        print("Please set the GOOGLE_MAPS_API_KEY environment variable.")
    else:
        ## TESTING since this worked
        
        # Define your origins and destinations
        origins = ["Hartland, MI", "Brighton, MI"]
        destinations = ["Ann Arbor, MI", "Novi, MI"]
    """""     
        origins_coords = [(42.6017, -83.6807),  # Example: Hartland, MI coordinates
                  (42.5336, -83.7828)]  # Example: Brighton, MI coordinates

destinations_coords = [(42.2808, -83.7430),  # Example: Ann Arbor, MI coordinates
                       (42.4817, -83.4758)]"""

## ////////////////////////////////////////////////////////// not needed?
        # Optional parameters (you can customize these)
       # travel_mode = "driving"
       # units = "imperial"  # or "metric"
#/////////////////////////////////////////////////////
        # Calculate the distance matrix
    distance_matrix_result = calculate_distance_matrix(
            api_key=api_key,
            origins=origins,
            destinations=destinations,
        )

        # Print the results
    if distance_matrix_result:
            print("Distance Matrix Results:")
            for i, row in enumerate(distance_matrix_result['rows']):
                for j, element in enumerate(row['elements']):
                    origin = origins[i]
                    destination = destinations[j]
                    status = element['status']
                    if status == 'OK':
                        distance = element['distance']['text']
                        duration = element['duration']['text']
                        print(f"From {origin} to {destination}:")
                        print(f"  Distance: {distance}")
                        print(f"  Duration: {duration}")
                    else:
                        print(f"From {origin} to {destination}: {status}")
    else:
            print("Failed to retrieve distance matrix results.")