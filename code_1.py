# SPDX-FileCopyrightText: 2018 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
from adafruit_motor import stepper 
import board
from analogio import AnalogIn
import digitalio
import pwmio
import simpleio
import lib.smoothing
 

pot = AnalogIn(board.A0)
STEPS = 200 
#limit = digitalio.DigitalInOut(board.D8) 
#limit.direction = digitalio.Direction.INPUT 
#limit.pull = digitalio.Pull.UP 

coils = (
    digitalio.DigitalInOut(board.D12),  # A1  #setup for the stepper
    digitalio.DigitalInOut(board.D11),  # A2
    digitalio.DigitalInOut(board.D9),   # B1
    digitalio.DigitalInOut(board.D10),  # B2
)


for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

smoothing = lib.smoothing.Smoothing()  #defining the library of smoothing.py in this file
Steps= 0 
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)


while True:
    # smoothvalue = int(simpleio.map_range(pot.value,0,65535,0,4500))
     
    #4500 end point of the range of the stepper
    smoothvalue = int(simpleio.map_range(smoothing.update(pot.value),0,65535,0,4500))   #Use smoothing to determine where the potentiometer is within our mapped range. 
    print("smoothvalue", smoothvalue, "   Steps" , Steps) 
    #print(limit.value) 
    time.sleep(.01)
    
    if abs(smoothvalue - Steps) >4: 
        #print(smoothvalue, Steps) 
        
        if smoothvalue > Steps:      #moving the stepper to the mapped and smoothed value and counting the steps
           motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
           Steps = Steps +1       
        time.sleep(.001)  


        if smoothvalue < Steps:       #moving the stepper backwards when neccesary. Also going to the smoothed and mapped value
           motor.onestep(style=stepper.DOUBLE, direction= stepper.FORWARD)
           Steps = Steps -1          
        time.sleep(.001) 
    


   
     
 
     
#while target != steps
    #if target is > steps
        #move stepper up one step and add 1 to steps 