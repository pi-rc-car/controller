import RPi.GPIO as GPIO

class Engine:

        def __init__(self, pins):
                self._pins=pins

                GPIO.setup(self._pins[0], GPIO.OUT)
                GPIO.setup(self._pins[1], GPIO.OUT)
                GPIO.setup(self._pins[2], GPIO.OUT)

                self._pwn = GPIO.PWM(self._pins[2], 100)
                self._pwm.start(100)

        def set_power(self, pwm=100.0):
                if pwm <= 0:
                        pwm = 0.1
                elif pwm > 100:
                        pwm = 100.0
                
                self._pwm.start(pwm)

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
