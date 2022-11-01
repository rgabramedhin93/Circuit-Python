import board
import time
import pwmio
import adafruit_motor.servo 
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

pwm = pwmio.PWMOut(board.D3, frequency=50)
pot = AnalogIn(board.A0)


while True:
    ``` 
    AnalogIn
     pot = analog_in.value

    angle = simpleio.map_range(pot, 0, 65535, 0, 180)

    my_servo.angle = angle

    time.sleep(0.1)
    ```
    