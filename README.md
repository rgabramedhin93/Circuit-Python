# CircuitPython
Welcome to my Circuit Python Page!
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

# Hello_CircuitPython

### Description & Code
This is the first CP assignment. We pretty much have to make the neopixel change colors. 


```python
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((255, 0, 0))
    time.sleep(1)
    dot.fill((0, 102, 0))
    time.sleep((1))
    dot.fill((0, 0, 255))
    time.sleep((1))

```


### Evidence
![rgb](https://raw.githubusercontent.com/rgabramedhin93/Circuit-Python/master/rgb%20color%20change.png)


### Wiring
![rgb](https://user-images.githubusercontent.com/112961430/193280272-701fa51d-ea67-4ab9-994e-ea3d98bdfe4a.png)
Image cred. https://github.com/egarcia28/CircuitPython#wiring

### Reflection
This assignment was petty fun to do. Making the neopixel light up and this also being my first circuit python assignment was pretty cool. Somethings that went wrong were trying to understand what the commands would do and also getting the code right. Overall I think I did pretty well. 




# CircuitPython_Servo

### Description & Code

```python
import time
import board
import pwmio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 30):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = 180
        time.sleep(0.05)
    for angle in range(180, 0, -30): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = 0
        time.sleep(0.05)

```

### Evidence
![title](https://drive.google.com/file/d/1CcqNxybahmtFGP3vWDXUN9-aFShGKLGD/view?usp=sharing)


### Wiring

### Reflection




# CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





# NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
