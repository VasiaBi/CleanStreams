import droneconnect, dronequit

# Connect with drone
tello = droneconnect.d_connect()

# Battery level for screen 2a
def get_battery_level():
    battery_level = tello.get_battery()
    # An integer between 0 and 100 is returned
    return battery_level
    # print ("Battery level: ", battery_level, " %") to test if it works

# Quit drone connection
dronequit.d_quit(tello)