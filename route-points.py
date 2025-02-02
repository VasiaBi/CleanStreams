import tello_sdk
import sqlite3
import json

# Route points for screen 2c
def route_points(flight_id):
    drone = tello_sdk.Tello()

    # Connect to the database. Need to replace database name
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()

    # Query to retrieve the JSON data
    # Assuming the table has the following columns: Autogenerted database ID, col_flight_name, col_flight_date, col_flight_time and col_route_points (JSON data)
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

    
