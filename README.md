# CircuitPython
Welcome to my Circuit Python Page!
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython_Motor Control](#CircuitPython_Motor_Control)
* [Circuit Python Distance Sensor](#CircuitPython_Distance_Sensor)
* [CircuitPython_TemperatureLCD](#CircuitPython_TemperatureLCD)
* [CircuitPython_RotaryEncoder](#CircuitPython_RotaryEncoder)
* [CircuitPython_Photointerrupter](#CircuitPython_Photointerrupter)
* [CAD_Test_Reflection](#CAD_Test_Reflection)
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
![alt text](https://raw.githubusercontent.com/rgabramedhin93/Circuit-Python/master/rgb%20color%20change%20(2).png)



### Wiring
![rgb](https://user-images.githubusercontent.com/112961430/193280272-701fa51d-ea67-4ab9-994e-ea3d98bdfe4a.png)
Image cred. https://github.com/egarcia28/CircuitPython#wiring

### Reflection
This assignment was pretty fun to do. Making the neopixel light up and this also being my first circuit python assignment was pretty cool. Somethings that went wrong were trying to understand what the commands would do and also getting the code right. Overall I think I did pretty well. 




# CircuitPython_Servo

### Description & Code
For this assignment, we are using circuit python to make a servo move. 
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
![ezgif-4-d46c662a38](https://user-images.githubusercontent.com/71406926/197799292-accaf38b-d874-4b74-a0c0-0d01c2c10cc7.gif)


### Wiring
![Servo wiring](https://user-images.githubusercontent.com/113116262/193041474-d091f6f6-306f-421a-9c83-9b513aab9223.png) wiring cred. https://github.com/jhelmke45/CircuitPython

### Reflection
Overall, this assignment was kind of hard. At first I had some problems with the code but I eventually figured it out. I got a lot of help from Holden, so I was able to do this assignment. Definitely something to look out for in the future is definitely looking over your code before you complete the assignment. 


# CircuitPython_LCD

### Description & Code

```python
// credit Jack Helmke
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
cur_state2 = True
prev_state2 = True
buttonPress = 0

while True:
    while btn2.value == False:
        lcd.set_cursor_pos(1,0)
        lcd.print("UP  ")
        cur_state = btn.value
        if cur_state != prev_state:
            if not cur_state:
                buttonPress = buttonPress + 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state = cur_state
    else:
        lcd.set_cursor_pos(1,0)
        lcd.print("DOWN")
        cur_state2 = btn.value
        if cur_state2 != prev_state2:
            if not cur_state2:
                buttonPress = buttonPress - 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state2 = cur_state2

```

### Evidence


https://user-images.githubusercontent.com/71406926/198095929-d65705ec-f77a-4a0e-8127-135f01dcfef2.mov



### Wiring
![LCD](https://raw.githubusercontent.com/rgabramedhin93/Circuit-Python/master/2%20button%20lcd%20wiring.png)
### Reflection
The LCD assingment was definitely the hardest Circuit Python assignment I've had to do. It took a while for me to do it, and a lot of coding. Sometimes the LCD wouldn't turn on, sometimes the code would just not work. It was pretty annoying. But I ended up getting inspiration from other classmates and used some of their code. One thing I learned is that if your having trouble, you can use other classmates code BUT with CREDIT. Overall, it was tough but I got through it with a lot of help.


# CircuitPython_Motor_Control
### Description & Code
For this assignment, we had to control a DC motor using a potentiometer. 

![Code](https://raw.githubusercontent.com/rgabramedhin93/Circuit-Python/master/process%20motor%20control%20code.png)

### Evidence

![Code](https://raw.githubusercontent.com/rgabramedhin93/Circuit-Python/master/process%20motor%20control%20code.png)


### Wiring

![Wiring](https://raw.githubusercontent.com/rgabramedhin93/Circuit-Python/master/motor%20control%20ss.png)

### Reflection
I got help with this assignment from Mr. Helmstetter a while ago. I just forgot to put it in my documentation. At first, I was struggling with getting the potentiometer wired up correctly. I eventually used some resources to get it wired good. Then getting the DC motor to be able to get controlled by the potentiometer was the hardest part. But I got and eventually finished it. 


# CircuitPython_Distance_Sensor

### Description & Code
For this assignment, we had to make the neopixel change colors depending on the distance you are from the ultrasonic sensor. 
```python
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio 
distance = 0

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5

while True:
    try:
        distance = sonar.distance 
        print((distance))
    except RuntimeError:
        print("oopsy daisy!")
    time.sleep(0.1) 
    if distance >= 5 and distance <= 20:
        simpleio.map_range(distance,5,20,0,255)
        dot.fill((0, 0, 255))
    else:
        dot.fill((255, 0, 0))
    if distance >= 0 and distance <= 5:
         simpleio.map_range(distance,5,0,255,0)
         dot.fill((0, 255, 0))

```

### Evidence


https://user-images.githubusercontent.com/71406926/198099247-39468172-9a51-47e3-b4e8-2d5562340257.mov


### Wiring
![Wiring](https://user-images.githubusercontent.com/112961430/197537630-7a8b370f-e29f-4c5f-ad99-c78c346eddf5.png)
Credit- https://github.com/kstanfo00/CircuitPython
### Reflection
Overall, this assignment was pretty fun to do. I liked that if depending on how far your finger is from the sensor, the color changes on the neopixel on the metro. In my opinion the assginment wasn't TOO hard, even though I had my struggles as always. I learned from it and now I feel good about it. One thing to look out for is in your code when you try to get the distance values correct. They are kind of confusing (well at least to me). 



# CircuitPython_TemperatureLCD
### Description & Code
For this assignment, we used an LCD to display the temperature coming from the temperature senor in Celcius and Farenheit. 
```python
import board
import time
import analogio
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
TMP36_PIN = board.A1  # Analog input connected to TMP36 output.
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

# turn on lcd power switch pin
lcdPower = digitalio.DigitalInOut(board.D8)
lcdPower.direction = digitalio.Direction.INPUT
lcdPower.pull = digitalio.Pull.DOWN

# Keep the I2C protocol from running until the LCD has been turned on
# You need to flip the switch on the breadboard to do this.
while lcdPower.value is False:
    print("still sleeping")
    time.sleep(0.1)

# Time to start up the LCD!
time.sleep(1)
print(lcdPower.value)
print("running")


# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)

# Loop forever.
while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    if temp_C > 9:
        lcd.print("too hot")
        print("too hot")
        lcd.clear()
        time.sleep(1)
        
    else:
        lcd.print("Brr too cold") 
        print("Brr too cold") 
        lcd.clear()
        time.sleep(1)


```

### Evidence
https://drive.google.com/file/d/1UMoYxz0ZRloDG47LyuzHOfMfm7gkT8hu/view?usp=share_link

### Wiring
![Wiring](https://raw.githubusercontent.com/rgabramedhin93/Circuit-Python/master/tmplcd%20pic%20wiring.png)

### Reflection
I think this assignment went pretty well, it was a nice challenge code wise because we had to be able to not only display the temperature coming from the sensor onto the LCD screen, but also showing the degrees in farenheit and celcius. 

# CircuitPython_RotaryEncoder
### Description & Code
For this assignment, we had to use a rotary encoder to make a traffic light and it also being displayed on an LCD. 
cred. [River](https://github.com/rivques/)
```python
import time
import rotaryio
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull


encoder = rotaryio.IncrementalEncoder(board.D3, board.D2)
last_position = 0
btn = DigitalInOut(board.D4)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
state = 0
Buttonyep = 1

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

ledGreen = DigitalInOut(board.D8)
ledYellow = DigitalInOut(board.D9)
ledRed = DigitalInOut(board.D10)
ledGreen.direction = Direction.OUTPUT
ledYellow.direction = Direction.OUTPUT
ledRed.direction = Direction.OUTPUT

while True:
    position = encoder.position
    if position != last_position:
        if position > last_position:
            state = state + 1
        elif position < last_position:
            state = state - 1
        if state > 2:
            state = 2
        if state < 0:
            state = 0
        print(state)
        if state == 0: 
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Go")
        elif state == 1:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Caution")
        elif state == 2:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Stop")
    if btn.value == 0 and Buttonyep == 1:
        print("buttion")
        if state == 0: 
                ledGreen.value = True
                ledRed.value = False
                ledYellow.value = False
        elif state == 1:
                ledYellow.value = True
                ledRed.value = False
                ledGreen.value = False
        elif state == 2:
                ledRed.value = True
                ledGreen.value = False
                ledYellow.value = False
        Buttonyep = 0
    if btn.value == 1:
        time.sleep(.1)
        Buttonyep = 1
    last_position = position

```
### Evidence
[Rotary Encoder Working](https://drive.google.com/file/d/1Hyd2WotE6Gq3mpgZ8H1b6dUIUOEAVpCy/view?usp=sharing)

### Wiring
cred. [Holden Austin]( https://github.com/haustin71/Circuit-Python#Rotary_Encoder)
![Wiring](https://raw.githubusercontent.com/haustin71/Circuit-Python/43b5247dc4f9c58f2804cb8cabea0733aec0314b/Images%20and%20Videos/RotaryEncoder%20Wiring%20Diagram.PNG)
### Reflection
Overall, I pretty much got the assignment from Holden. I was struggling with it, and he helped me finish it. The assignment itself is pretty cool. Using a Rotary Encoder to make a traffic light and displaying it on an LCD screen seems pretty cool and it was kind of fun to play with. 



# CircuitPython_Photointerrupter
### Description & Code
For this assignment, I have to wire up a photo interrupter so that an LED will light up when I put something on between the legs of the interrupter.

```python
import board
import digitalio
import time

led_pin = digitalio.DigitalInOut(board.D8)
led_pin.direction = digitalio.Direction.OUTPUT

int_pin = digitalio.DigitalInOut(board.D3)
int_pin.switch_to_input(pull=digitalio.Pull.UP)

pp = 0
old_pp = 0

def blink(channel):
    global pp
    global state
    state = not state
    pp += 1

int_pin.irq(trigger=digitalio.EdgeChange, handler=blink)

state = False
while True:
    led_pin.value = state
    if old_pp != pp:
        print(pp)
    old_pp = pp
    time.sleep(0.01)
    
```
### Evidence/Wiring
![Evidence = Wiring](https://raw.githubusercontent.com/rgabramedhin93/Circuit-Python/master/Photointerrupter.png)

### Reflection
Overall this assignment is kind of cool, It wasn't too hard but I did have some trouble with some of the code. Now that I know how to use this, I think I could possibly incorporate this into a future project. It's easy to wire up and I think that I wouldn't have a problem with getting this to work.


# CAD_Test_Reflection
I personally thought it was pretty hard, and obviously I think other people agree. I unfortunatley didn't pass the exam, and didn't retake it either. I just didn't feel like I would do better, and I just didn't want to take it again. I think maybe we could have started to prep for the test earlier, because I was still confused on some of the aspects. Overall, I could have reached out on a couple of more occasions to fully capture what I had to do. 



