from djitellopy import Tello
import flightdistance, flightangle, routepoints, droneconnect, dronequit
import videostream

# Connect with drone
tello = droneconnect.drone_connect()

def fly_drone():

    # Drone takeoff after 
    tello.takeoff()
    # print("Drone takeoff") to test if it works

    # small pause before executing the next command
    # time.sleep(5)

    # Get start and end points from routepoints.py
    start_point = routepoints()[1]
    end_point = routepoints()[2]
    # print(start_point, end_point) to test if it works

    # Calculate required movement
    move_distance = flightdistance.distance(start_point[0], start_point[1], end_point[0], end_point[1])
    move_angle = flightangle.angle(start_point[0], start_point[1], end_point[0], end_point[1])

    # Rotate to the correct direction (to face end point)
    tello.rotate_clockwise(int(move_angle))
    # print("Drone rotated towards destination") to test if it works

    # small pause before executing the next command
    # time.sleep(5)

    # Start video stream
    videostream.stream_on()

    # Move forward (max movement is ~500 cm per command)
    remaining_distance = move_distance
    while remaining_distance > 0:
        move_distance = min(500, remaining_distance)  # Move in steps of 500 cm
        tello.move_forward(int(move_distance))
        remaining_distance -= move_distance

        # small pause before executing the next command
        # time.sleep(5)
     
    # Rotate torards the opposit direction (to face start point)
    tello.rotate_clockwise(180)
    # print("Drone rotated 180°") to test if it works

    # Move back to the start point
    remaining_distance = move_distance
    while remaining_distance > 0:
        move_distance = min(500, remaining_distance)  # Move in steps of 500 cm
        tello.move_forward(int(move_distance))
        remaining_distance -= move_distance

    # small pause before executing the next command
    # time.sleep(5)

    # Stop video stream
    videostream.stream_off()

    # Land drone
    tello.land()
    # print("Drone landed successfully") to test if it works





# tello.move_up(x)
# tello.streamon()
# tello.move (direction, x)
# tello.move_back(x)
# tello.streamoff()
# tello.land()

# Quit drone connection
dronequit.drone_quit(tello)


