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

# Quit drone connection
def drone_quit(drone):
    drone.quit()

# Battery level for screen 2a
def get_battery_level():
    drone = tello_sdk.Tello()
    battery_level = drone.get_battery()
    return battery_level

# Remaining flight time for screen 2a
def remaining_flight_time():
    drone = tello_sdk.Tello()
    #If percentage is returned, then "/100" is not needed
    rem_flight_time = max_flight_time*get_battery_level/100
    return rem_flight_time

# Route points for screen 2c
def get_starting_point():
    drone = tello_sdk.Tello()

    # Connect to the database. Need to replace database name
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()

    # Query to retrieve the JSON data
    # Assuming the table has two columns, ID and route_points
    # Replace table name (flights) and column name (route_points).
    # ID: Can we use the flight name combined with the flight time sto that it is unique?
    cursor.execute("SELECT route_points FROM flights WHERE id = ?", (id,))
    result = cursor.fetchone()

    # A result of this type is expected: (ID, '{"route_points": [coord1, coord2, coord3, etc]}')
    if result:
        route_points = json.loads(result[1])
        return route_points
    
    # Show route point on the map

    # Example usage
    for point in route_data['points']:  # Assuming JSON has a key 'points'
        print(f"Point: Latitude={point['lat']}, Longitude={point['lon']}")

    # Close the connection
    conn.close()

    # Next point
