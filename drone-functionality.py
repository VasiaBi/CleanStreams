import tello_sdk
import sqlite3
import json

# Maximum flight time (0 wind / consistent 15kph) for DJI Tello 2.0 in minutes
max_flight_time = 13

# Connect with drone
def drone_connect():
    drone = tello_sdk.Tello()
    drone.connect()
    return drone
    # print ("Drone connected")

# Quit drone connection
def drone_quit(drone):
    drone.quit()
    # print ("Drone disconnected")

# Battery level for screen 2a
def get_battery_level():
    drone = tello_sdk.Tello()
    battery_level = drone.get_battery()
    return battery_level
    # print ("Battery level: ", battery_level)

# Remaining flight time for screen 2a
def remaining_flight_time():
    drone = tello_sdk.Tello()
    #If percentage is returned, then "/100" is not needed
    rem_flight_time = max_flight_time*get_battery_level()/100
    return rem_flight_time
    # print ("Remaining flight time: ", rem_flight_time)

# Add flight name for screen 2b
# Do we get the name through python and store it to the database? 
# Then the flight name and flight notes should be added to the database so that we can get the flight_id


# Route points for screen 2c
def get_starting_point(flight_id):
    drone = tello_sdk.Tello()

    # Connect to the database. Need to replace database name
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()

    # Query to retrieve the JSON data
    # Assuming the table has two columns, col_flight_id and col_route_points
    # Replace table name (table_flights) and column names (col_flight_id, col_route_points)
    # col_flight_id: Can we use the flight name combined with current date and time so that it is unique?
    # example col_flight_id
    cursor.execute("SELECT col_route_points FROM table_flights WHERE col_flight_id = ?", (flight_id,))
    result = cursor.fetchone()

    # A result of this type is expected: (ID, '{"route_points": [coord1, coord2, coord3, etc]}')
    if result:
        route_points = json.loads(result[0])
        return route_points
    else:
        return None
    
    # Show route point on the map

    # Example usage
    for point in route_data['points']:  # Assuming JSON has a key 'points'
        print(f"Point: Latitude={point['lat']}, Longitude={point['lon']}")

    # Close the connection
    conn.close()

    
