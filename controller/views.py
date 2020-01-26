from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

import car_control

def power(request):

    try:
        power = request.GET['power']
    except MultiValueDictKeyError:
        power = -1


    return HttpResponse(f"power={power}")


def action(request):
    try:
        action = request.GET['action']
    except MultiValueDictKeyError:
        action = -1

    return HttpResponse(f"action={action}")

