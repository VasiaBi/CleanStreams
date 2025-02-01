import tello_sdk

# Connect with drone
def drone_connect():
    drone = tello_sdk.Tello()
    drone.connect()
    return drone
    # print ("Drone connected")

# Get the flight name and flight notes (screen 2b) and store it to the database
# Also get current dat and time
# Database ID is created

# Quit drone connection
def drone_quit(drone):
    drone.quit()
    # print ("Drone disconnected")