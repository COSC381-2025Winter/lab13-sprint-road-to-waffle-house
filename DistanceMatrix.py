from googlemaps import convert ## idk if this is really needed 
import googlemaps
from where_is_waffle_house import *

def getUserAddress():
    ####RYAN
    #prompts user for location you are at
    return input("Enter to your location: ")

def main():
    api_key = "AIzaSyC2UHZ50CgCeueKLSZsp5NS7rJnUrj38gA"
   
        
    """""
        ## We can pass origins in this format or via coordinates, currently set up for coords
        # But if we go back to the names we have to change the printing variables.
        """""
        # Define your origins and destinations
        #origins = ["Hartland, MI", "Brighton, MI"]
        #destinations = ["Ann Arbor, MI", "Novi, MI"]
    done = False
    while not done:
        yourLocation = getUserAddress()
            # Define your origins and destinations
        origins_coords = [yourLocation]
        
        #origins_coords = [(42.6017, -83.6807),  # Example: Hartland, MI coordinates
                            #(42.5336, -83.7828)]  # Example: Brighton, MI coordinates

        destinations_coords = [get_waffle_house_location(yourLocation).get("formatted_address")] #(closest waffle house)
        #REPLACE WITH JOES API CALL

    ## ////////////////////////////////////////////////////////// not needed?
            # Optional parameters (you can customize these)
        # travel_mode = "driving"
        # units = "imperial"  # or "metric"
    #/////////////////////////////////////////////////////
        """""
            Calculate the distance matrix by calling the function
            Since we everything but api key, origins and destinations have default values
            in 
            """
        distance_matrix_result = calculate_distance_matrix(
                api_key=api_key,
                origins=origins_coords,
                destinations=destinations_coords,
            )
        # print(distance_matrix_result) ///////// use this if you want to see default output

            # Print the results
        if distance_matrix_result:
                print("Distance Matrix Results:")
                for i, row in enumerate(distance_matrix_result['rows']):
                    for j, element in enumerate(row['elements']):
                        origin = origins_coords[i]
                        destination = destinations_coords[j]
                        status = element['status']
                        if status == 'OK':
                            distance = element['distance']['text']
                            duration = element['duration']['text']
                            print(f"From {origin} to {destination}:")
                            print(f"  Distance: {distance}")
                            print(f"  Duration: {duration}")
                            done = True
                        else:
                        #   print(f"From {origin} to {destination}: {status}")
                            print("Location not found, try again (Hint: Putting the state such as MI at the end helps)\n")
                            done = False
    # else:
        #  print("Failed to retrieve distance matrix results.")
# import os 
"""""/\
this is only used to hide key,the function is on line #118 and involves
storing the key on your system, idk if we really want that 
"""
#Gets travel distance and time for a matrix of origins and destinations.
def calculate_distance_matrix(api_key, origins, destinations,mode=None,
                              language=None, avoid=None, units="imperial",
                              departure_time=None, arrival_time=None, transit_mode=None,
                              transit_routing_preference=None, traffic_model=None, region=None):
    
    """ Just documentation from the repo that we can use. it states all parameters above, 
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
   
    :type language: string   }

   { :param avoid: Indicates that the calculated route(s) should avoid the
        indicated features. Valid values are "tolls", "highways" or "ferries".
        
    :type avoid: string   }

    { :param units: Specifies the unit system to use when displaying results.
        Valid values are "metric" or "imperial".
        
    :type units: string }

    { :param departure_time: Specifies the desired time of departure.
    
    :type departure_time: int or datetime.datetime  }

   { :param arrival_time: Specifies the desired time of arrival for transit
        directions. Note: you can't specify both departure_time and
        arrival_time.
    :type arrival_time: int or datetime.datetime }

    { :param transit_mode: Specifies one or more preferred modes of transit.
        This parameter may only be specified for requests where the mode is
        transit. Valid values are "bus", "subway", "train", "tram", "rail".
        "rail" is equivalent to ["train", "tram", "subway"].
        
    :type transit_mode: string or list of strings  }

    { :param transit_routing_preference: Specifies preferences for transit
        requests. Valid values are "less_walking" or "fewer_transfers".
        
    :type transit_routing_preference: string }

    :param traffic_model: Specifies the predictive travel time model to use.
        Valid values are "best_guess" or "optimistic" or "pessimistic".
        The traffic_model parameter may only be specified for requests where
        the travel mode is driving, and where the request includes a
        departure_time.

    { :param region: Specifies the prefered region the geocoder should search
        first, but it will not restrict the results to only this region. Valid
        values are a ccTLD code.
        
    :type region: string  }

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
            transit_mode = transit_mode,
            traffic_model=traffic_model,
           transit_routing_preference= transit_routing_preference
        )
        # error handling 
        print("API successfully executed ")
        return result
    #except googlemaps.exceptions.ApiError as e:
     #   print(f"An API error occurred: {e}")
     #   return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
if __name__ == "__main__":
    main()

    # Replace with your actual Google Maps Platform API key
   # api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
   
