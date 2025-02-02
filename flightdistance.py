import routepoints
import math

# Get start and end points from routepoints.py
start_point = routepoints()[1]
end_point = routepoints()[2]
# print(start_point, end_point) to test if it works

# Break down the coordinates for start_point, assuming they are in the format: (latitude, longitude)
lat_start = start_point[0]
lon_start = start_point[1]

# Break down the coordinates for end_point, assuming they are in the format: (latitude, longitude)
lat_end = end_point[0]
lon_end = end_point[1]

# Note: Haversine formula can be used to take into account the Earth's curvative
# But given the drone's technical specs (flight duration) and the low flying height (for better image processing) I assume we can use the Euclidean distance formula for simplification purposes

# Calculate distance between the two points using the Euclidean distance formula
def distance(lat_start, lon_start, lat_end, lon_end):
    distance_in_degrees = math.sqrt((lat_end - lat_start) ** 2 + (lon_end - lon_start) ** 2)

    # Convert distance from degrees to meters
    flight_distance = distance_in_degrees * 111000

    return flight_distance
    # print(flight_distance) to test if it works

