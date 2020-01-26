from django.http import HttpResponse
from sys import stderr

from car_control.car import set_power, roll_front, roll_back, turn_right, turn_left, stop

def power(request):

    try:
        power = float(request.GET['power'])
        if power > 100:
            power = 100.0
        elif power <= 0:
            power = 0.1

        set_power(power)
    except Error as e:
        print(e, file=stderr)
        return HttpResponse("please specify the power parameter")

    return HttpResponse(f"the pwm duty cycle has successfully been updated to {power}%")


def action(request):
    try:
        action = request.GET['action']

        if action == 'stop':
            stop()
        elif action == 'roll_front':
            roll_front()
        elif action == 'roll_back':
            roll_back()
        elif action == 'turn_right':
            turn_right()
        elif action == 'turn_left':
            turn_left()
        else:
            return HttpResponse(f"action {action} not found.")

    except Error as e:
        print(e, file=stderr)
        return HttpResponse("please specify the action parameter")

    return HttpResponse(f"action {action} executed succesfully")

