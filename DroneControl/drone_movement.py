import time

from dronekit import connect
from dronekit import VehicleMode

from movement_helpers import *

vehicle = None
drone_height = 5

def print_altitude():
    global vehicle
    print("Altitude: %.2f" % (vehicle.location.global_relative_frame.alt))

def check_drone():
    global vehicle
    print("Waiting for drone to be armable...")
    while not vehicle.is_armable:
        time.sleep(1)
    print("Drone can now be armed!")

def arm_drone():
    global vehicle
    print("\nArming the motor")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    print("\nWaiting to be armed...")
    while not vehicle.armed:
        time.sleep(0.5)
    print("Drone armed!")
    

def takeoff_to_altitude(altitude):
    global vehicle
    print("\nTaking off the drone to 10m...")
    vehicle.simple_takeoff(drone_height)

    while True:
        print_altitude()

        if (vehicle.location.global_relative_frame.alt >= 0.95 * drone_height):
            print("Reached desired altitude of %d" % (drone_height))
            break

        time.sleep(0.5)

def land_drone():
    global vehicle
    print("\nLanding drone...")
    vehicle.mode = VehicleMode("LAND")

    while True:
        print_altitude()

        if (vehicle.location.global_relative_frame.alt <= 0.05):
            print("Reached desired altitude of %d" % (0))
            break

        time.sleep(0.5)

def main():
    global vehicle
    vehicle = connect('localhost:14551', wait_ready=True)
    
    # Takeoff the drone
    check_drone()
    arm_drone()
    takeoff_to_altitude(drone_height)

    # Pause for 5s
    time.sleep(5)

    DURATION = 3
    SPEED_BASE = 1
    NORTH =  SPEED_BASE      # North
    SOUTH = -SPEED_BASE      # South
    EAST  =  SPEED_BASE      # East
    WEST  = -SPEED_BASE      # West
    UP    = -0.5             # Up  
    DOWN  =  0.5             # Down    
    
    print("Moving drone by (10, 10)")
    goto_position_target_local_ned(vehicle, 1, 1, -10)
    print("Movement complete.")

    time.sleep(20)

    print("Moving drone by (10, 10)")
    goto_position_target_local_ned(vehicle, 0, 0, -9)
    print("Movement complete.")
    
    time.sleep(20)
    
    '''
    print("Rotating drone...")
    condition_yaw(vehicle, 90, True)
    print("Rotation complete.")
    
    print("Moving down...")
    send_ned_velocity(vehicle, 0, 0, DOWN, 1.0)
    print("Movement complete.")

    time.sleep(5)
    
    print("Moving NE...")
    send_ned_velocity(vehicle, NORTH, EAST, 0, 10.0)
    print("Movement complete.")

    time.sleep(5)
    
    print("Moving SE...")
    send_ned_velocity(vehicle, SOUTH, EAST, 0, 10.0)
    print("Movement complete.")

    time.sleep(5)
    
    print("Moving SW...")
    send_ned_velocity(vehicle, SOUTH, WEST, 0, 10.0)
    print("Movement complete.")

    time.sleep(5)
    
    print("Moving NW...")
    send_ned_velocity(vehicle, NORTH, WEST, 0, 10.0)
    print("Movement complete.")
    '''

    # Pause for 5s
    time.sleep(5)
    
    # Land the drone
    land_drone()

    # Exit
    vehicle.close()
    exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting...")
        vehicle.close()
        exit(1)



