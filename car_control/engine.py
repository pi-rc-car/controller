import RPi.GPIO as GPIO

class Engine:

        def __init__(self, In1, In2, En, mode=GPIO.BCM):
                self._In1 = In1
                self._In2 = In2
                self._En = En

                GPIO.setmode(mode)
                GPIO.setup(self._In1, GPIO.OUT)
                GPIO.setup(self._In2, GPIO.OUT)
                GPIO.setup(self._En, GPIO.OUT)

                self._pwn = GPIO.PWM(self._En, 100)
                self._pwm.start(100)

        def set_power(self, pwm=100.0):
                if pwm <= 0:
                        pwm = 0.1
                elif pwm > 100:
                        pwm = 100.0
                
                self._pwm.start(pwm)

        def reset(self):
                self._pwm.stop()
                GPIO.output(self._In1, GPIO.LOW)
                GPIO.output(self._In2, GPIO.LOW)
                GPIO.output(self._En, GPIO.LOW)

        def go_forward(self):
                GPIO.output(self._In1, GPIO.HIGH)
                GPIO.output(self._In2, GPIO.LOW)
                GPIO.output(self._En, GPIO.HIGH)
        
        def go_backward(self):
                GPIO.output(self._In1, GPIO.LOW)
                GPIO.output(self._In2, GPIO.HIGH)
                GPIO.output(self._En, GPIO.HIGH)
