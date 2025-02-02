import tello_sdk
import sqlite3
import json
import math

# User has given the location coordinates and they are stored in the database (handled from the front or from Python?)
# A pin appears on the map for each given coordinate (handled from the front?)
# Assuming the coordinates have been stored in the database, we can retrieve them and show them on the map
# The following code will get the starting point and the destination point from the database and calculate the distance and the duration of the flight


# Distance between the two points, assuming coordinates are in the format: (latitude, longitude)
# Haversine formula can be used to take into account the Earth's curvative
# But given the drone's technical specs (flight duration) and the low flying height (for better image processing) we can also use the Euclidean distance formula for simplification purposes
# Do we get the flight_id from the front?
def distance(col_flight_id):

    # Connect to the database. Need to replace database name
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()

    # Query to retrieve the JSON data
    # Assuming the table has the following columns: col_flight_id (autogenerted from database), col_flight_name, col_flight_date, col_flight_time and col_route_points (JSON data)
    # Replace table name (table_flights) and column names (col_flight_id, col_route_points)
    cursor.execute("SELECT col_flight_name, col_route_points FROM table_flights WHERE col_flight_id = ?", (col_flight_id,))
    result = cursor.fetchone()

    # Close connection after fetching data
    conn.close()

    # A result of this type is expected: (col_flight_id, '{"route_points": [coord1, coord2]}')
    if result:
        # Give the name to the front so that it can be displayed as the title on screen 3c
        flight_name = result[0]
        route_points = json.loads(result[1])

        # Assuming we only have 2 coordinates, the start point and the end point
        start_point = route_points['route_points'][0]
        end_point = route_points['route_points'][1]

        lat_start = start_point[0]
        lon_start = start_point[1]
        lat_end = end_point[0]
        lon_end = end_point[1]

        # The distance is in units, should be converted to kilometers
        flight_distance = math.sqrt((lat_end - lat_start) ** 2 + (lon_end - lon_start) ** 2)

        # Assuming an average speed of 15kph
        flight_duration = flight_distance / 15

        # Return to front for screen 3c
        return flight_name, route_points, flight_distance, flight_duration
    
    else:
        return None, None
    


        
#starting_point = JSON[0]
#drone start flight
#- takeoff

#end_point = JSON[1]
#drone end flight
#- land

#route = x km

#start flight 
#move

# Route points for screen 2c
#def route_points(flight_id):
    drone = tello_sdk.Tello()
   
