import droneconnect, dronequit, battery

# Maximum flight time (0 wind / consistent speed 15kph) for DJI Tello 2.0 in minutes
max_flight_time = 13

battery_level = battery.get_battery_level()

# Remaining flight time for screen 2a
def remaining_flight_time(battery_level):
    rem_flight_time = max_flight_time*battery_level/100
    return rem_flight_time
    # print ("Remaining flight time: ", rem_flight_time) to test if it works