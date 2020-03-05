import RPi.GPIO as GPIO

class Engine:

        def __init__(self, pins, mode=GPIO.BCM):
                self._pins=pins
                
                GPIO.setmode(mode)
                GPIO.setup(self._pins[0], GPIO.OUT)
                GPIO.setup(self._pins[1], GPIO.OUT)
                GPIO.setup(self._pins[2], GPIO.OUT)

                self._pwm = GPIO.PWM(self._pins[2], 100)
                self._pwm.start(100)
                print(f"setup pins {self._pins}")

        def set_power(self, pwm=100.0):
                if pwm <= 0:
                        pwm = 0.1
                elif pwm > 100:
                        pwm = 100.0
                
                self._pwm.start(pwm)
                print(f"set pwm at {pwm}")

        def reset(self):
                self._pwm.stop()
                GPIO.output(self._pins[0], GPIO.LOW)
                GPIO.output(self._pins[1], GPIO.LOW)
                GPIO.output(self._pins[2], GPIO.LOW)

        def go_forward(self):
                GPIO.output(self._pins[0], GPIO.HIGH)
                GPIO.output(self._pins[1], GPIO.LOW)
                GPIO.output(self._pins[2], GPIO.HIGH)
        
        def go_backward(self):
                GPIO.output(self._pins[0], GPIO.LOW)
                GPIO.output(self._pins[1], GPIO.HIGH)
                GPIO.output(self._pins[2], GPIO.HIGH)
