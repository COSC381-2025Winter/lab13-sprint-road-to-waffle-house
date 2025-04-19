import pytest
from distance_matrix import *

@ pytest.fixture
def sample_data():
      return {
        "api_key": "AIzaSyC2UHZ50CgCeueKLSZsp5NS7rJnUrj38gA",
        "origins":["Hartland, MI", "Brighton, MI"],
        "destinations": ["Ann Arbor, MI", "Novi, MI"],
        "mode": "",
        "language": "",
        "avoid": "",
        "units": "",
        "departure_time": "",
        "arrival_time": "",
        "transit_mode": "",
        "transit_routing_preference": "",
        "traffic_model":"",
        "region": "",
    }


def test_calculate_distance_matrix_basic(sample_data,capsys):
    #act 
    api_key = sample_data["api_key"]
    origins = sample_data["origins"]
    destinations = sample_data["destinations"]
 
    calculate_distance_matrix(api_key,origins,destinations)
    
    captured = capsys.readouterr().out
    #assert
    assert "API successfully executed " in captured
    
def test_calculate_distance_matrix_Distance(sample_data,capsys):
    #act 
    api_key = sample_data["api_key"]
    origins = sample_data["origins"]
    destinations = sample_data["destinations"]
 

    
    result = calculate_distance_matrix(api_key,origins,destinations)
    for i, row in enumerate(result['rows']):
                for j, element in enumerate(row['elements']):
                    origin = origins[i]
                    destination = destinations[j]
                    status = element['status']
                    if status == 'OK':
                        distance = element['distance']['text']
                        duration = element['duration']['text']
    #assert
    assert "16.7 mi" in distance
    
def test_bad_api_key(sample_data, capsys):
      #act 
    api_key = "who needs a key? lets try a lockpick"
    origins = sample_data["origins"]
    destinations = sample_data["destinations"]
 
    calculate_distance_matrix(api_key,origins,destinations)
    
    captured = capsys.readouterr().out
    #assert
    assert "API successfully executed "  not in captured
    assert "An unexpected error occurred: Invalid API key provided." in captured
    
def test_origin_does_not_exist(sample_data, capsys):
    #act 
    api_key = sample_data["api_key"]
    origins = sample_data["origins"]
    destinations = "An ihop"
    result = calculate_distance_matrix(api_key,origins,destinations)
    for i, row in enumerate(result['rows']):
                for j, element in enumerate(row['elements']):
                    origin = origins[i]
                    destination = destinations[j]
                    status = element['status']
                    if status == 'OK':
                        distance = element['distance']['text']
                        duration = element['duration']['text']
    captured = capsys.readouterr().out
    #assert
    assert "API successfully executed " in captured
    assert 'status' in element and element['status'] == 'NOT_FOUND'

def test_destinations_does_not_exist(sample_data, capsys):
    #act 
    api_key = sample_data["api_key"]
    origins = "My house"
    destinations = sample_data["destinations"]
    
    result = calculate_distance_matrix(api_key,origins,destinations)
    for i, row in enumerate(result['rows']):
                for j, element in enumerate(row['elements']):
                    origin = origins[i]
                    destination = destinations[j]
                    status = element['status']
                    if status == 'OK':
                        distance = element['distance']['text']
                        duration = element['duration']['text']
    captured = capsys.readouterr().out
    #assert
    assert "API successfully executed " in captured
    assert 'status' in element and element['status'] == 'NOT_FOUND'
    
def test_destinations_is_bad(sample_data, capsys):
    #act 
    api_key = sample_data["api_key"]
    origins = sample_data["origins"]
    destinations = (0,0)
    
    result = calculate_distance_matrix(api_key,origins,destinations)
    for i, row in enumerate(result['rows']):
                for j, element in enumerate(row['elements']):
                    origin = origins[i]
                    destination = destinations[j]
                    status = element['status']
                    if status == 'OK':
                        distance = element['distance']['text']
                        duration = element['duration']['text']
    captured = capsys.readouterr().out
    #assert
    assert "API successfully executed " in captured
    assert 'status' in element and element['status'] == 'ZERO_RESULTS'
    
def test_origins_is_bad(sample_data, capsys):
    #act 
    api_key = sample_data["api_key"]
    origins = (0,0)
    destinations = sample_data["destinations"]
    
    result = calculate_distance_matrix(api_key,origins,destinations)
    for i, row in enumerate(result['rows']):
                for j, element in enumerate(row['elements']):
                    origin = origins[i]
                    destination = destinations[j]
                    status = element['status']
                    if status == 'OK':
                        distance = element['distance']['text']
                        duration = element['duration']['text']
    captured = capsys.readouterr().out
    #assert
    assert "API successfully executed " in captured
    assert 'status' in element and element['status'] == 'ZERO_RESULTS'
    
def test_main_processes_data(capsys, monkeypatch):
    # Assuming main() processes some default, real, location and prints a result
        
        monkeypatch.setattr("builtins.input", lambda _: "Ann Arbor, MI")
        main()

        captured = capsys.readouterr()
        output = captured.out
        
        assert "Distance" in output  # Check for a starting message
        assert "Duration" in output

def test_main_incorrect_location(capsys, monkeypatch):
    # gives main an incorrect location to see if it loops
    responses = iter(["Not Real Place", "Ann Arbor, MI"])
    monkeypatch.setattr("builtins.input", lambda msg: next(responses))
    main()

    captured = capsys.readouterr()
    output = captured.out
    
    assert "Location not found, try again" in output  # Check for the incorrect location
    assert "Distance" in output   # Check for the correct location then being found
    assert "Duration" in output

    # Add more specific assertions based on the expected output of main()

def test_getUserAddress(monkeypatch):
    # tests the getUserAddress function that gets the users address
        monkeypatch.setattr("builtins.input", lambda _: "Ann Arbor, MI")
        output = getUserAddress()

        assert "Ann Arbor, MI" in output              
    
    
# test to see if api key works 
# test to see if it gets a location
# test to see if errors work well 



        #destinations 