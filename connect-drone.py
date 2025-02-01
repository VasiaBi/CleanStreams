import tello_sdk

# Connect with drone
def drone_connect():
    drone = tello_sdk.Tello()
    drone.connect()
    return drone
    # print ("Drone connected") to test if it works