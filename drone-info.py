import tello_sdk

# Maximum flight time (0 wind / consistent 15kph) for DJI Tello 2.0 in minutes
max_flight_time = 13

# Connect with drone
def drone_connect():
    drone = tello_sdk.Tello()
    drone.connect()
    return drone
    # print ("Drone connected")

# Battery level for screen 2a
def get_battery_level():
    drone = tello_sdk.Tello()
    battery_level = drone.get_battery()
    return battery_level
    # print ("Battery level: ", battery_level) to test if it works

# Remaining flight time for screen 2a
def remaining_flight_time():
    drone = tello_sdk.Tello()
    #If percentage is returned, then "/100" is not needed
    rem_flight_time = max_flight_time*get_battery_level()/100
    return rem_flight_time
    # print ("Remaining flight time: ", rem_flight_time) to test if it works