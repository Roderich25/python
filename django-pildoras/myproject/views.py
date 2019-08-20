from django.http import HttpResponse


def greeting(request):
    return HttpResponse("Hello World! This is my first Django web page.")


def farewell(request):
    return HttpResponse("Good bye, my friend!")
