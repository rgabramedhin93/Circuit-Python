import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5

while True:
    try:
        distance = sonar.distance 
        print((distance))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1) 
    if sonar.distance > 20:
        dot.fill((0, 255, 0))
    else:
        dot.fill((0, 0, 255))
    if sonar.distance < 20 and sonar.distance > 5:
        dot.fill((0, 0, 255))
        

    



