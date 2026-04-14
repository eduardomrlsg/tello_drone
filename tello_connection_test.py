from djitellopy import Tello

tello = Tello()

print("Connecting to Tello...")
tello.connect()
print("Battery level:", tello.get_battery())

print("Taking off...")
tello.takeoff()

tello.move_up(50)

print("Landing...")
tello.land()
tello.end()