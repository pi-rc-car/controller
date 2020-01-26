import RPi.GPIO as GPIO

from engine import Engine


DEFAULT_POWER=0.1

engines = []

TOP_RIGHT_MOTOR=0
TOP_LEFT_MOTOR=1
BOTTOM_RIGHT_MOTOR=2
BOTTOM_LEFT_MOTOR=3

def setup():
    #set default pins for engines
    engines.append(Engine((0, 0, 0)))
    engines.append(Engine((0, 0, 0)))
    engines.append(Engine((0, 0, 0)))
    engines.append(Engine((0, 0, 0)))

    #set board mode
    GPIO.setmode(GPIO.BCM)

def set_power(power=100.0):
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