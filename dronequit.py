from djitellopy import Tello

# Quit drone connection
def d_quit(tello):
    tello.end()
    # print ("Drone disconnected") to test if it works