import RPi.GPIO as GPIO

from .engine import Engine


DEFAULT_POWER=0.1

engines = []

TOP_LEFT_MOTOR=0
TOP_RIGHT_MOTOR=1
BOTTOM_LEFT_MOTOR=2
BOTTOM_RIGHT_MOTOR=3

def setup():
    #set default pins for engines
    engines.append(Engine((16, 20, 21)))
    engines.append(Engine((13, 19, 26)))
    engines.append(Engine((2, 3, 4)))
    engines.append(Engine((17, 27, 22)))

    #set board mode
    GPIO.setmode(GPIO.BCM)
    stop()

def set_power(power=100.0):
    if power > 100:
        power = 100.0
    elif power <= 0:
        power = 0.1
        
    for engine in engines:
        engine.set_power(power)

def roll_front():
    for engine in engines: 
        engine.go_forward()

def roll_back():
    for engine in engines: 
        engine.go_backward()

def turn_right():
    engines[TOP_LEFT_MOTOR].go_forward()
    engines[TOP_RIGHT_MOTOR].go_backward()
    engines[BOTTOM_LEFT_MOTOR].go_forward()
    engines[BOTTOM_RIGHT_MOTOR].go_backward()

def turn_left():
    engines[TOP_LEFT_MOTOR].go_backward()
    engines[TOP_RIGHT_MOTOR].go_forward()
    engines[BOTTOM_LEFT_MOTOR].go_backward()
    engines[BOTTOM_RIGHT_MOTOR].go_forward()

def stop():
    for engine in engines: 
        engine.reset()
