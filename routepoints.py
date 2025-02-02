import sqlite3
import json

# User has given the location coordinates and they are stored in the database (handled from the front or from Python?)
# A pin appears on the map for each given coordinate (handled from the front?)
# Assuming the coordinates have been stored in the database, we can retrieve them and show them on the map
# The following code will get the starting point and the destination point from the database and calculate the distance and the duration of the flight


# Do we get the flight_id from the front?
def route_points(col_flight_id):

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

        return flight_name, start_point, end_point
        # print(flight_name, start_point, end_point) to test if it works
    
    else:
        return None, None
    