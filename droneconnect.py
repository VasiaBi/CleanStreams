from djitellopy import Tello

# Connect with the drone
def d_connect():
    tello = Tello()
    tello.connect()
    return tello
    # print ("Drone connected") to test if it works