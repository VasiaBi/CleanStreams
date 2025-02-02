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

# Calculate angle of the two points
def angle(lat_start, lon_start, lat_end, lon_end):

    # Calculate dx and dy and convert to meters
    dx = lon_end - lon_start * 111000
    dy = lat_end - lat_start * 111000

    angle = math.degrees(math.atan2(dy, dx))
    return angle
    # print(angle) to test if it works

