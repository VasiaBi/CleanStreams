import tello_sdk
import sqlite3
import json

# Battery level for screen 2a
def get_battery_level():
    drone = tello_sdk.Tello()
    battery_level = drone.get_battery()
    return battery_level
    # print ("Battery level: ", battery_level)