from django.http import HttpResponse


def action(request):
    return HttpResponse("Hello, World!")

