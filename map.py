from djitellopy import Tello


# Connect with drone
def drone_connect():
    drone = Tello()
    drone.connect()
    return drone
    # print ("Drone connected") to test if it works