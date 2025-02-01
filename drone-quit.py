import tello_sdk

# Quit drone connection
def drone_quit(drone):
    drone.quit()
    # print ("Drone disconnected") to test if it works