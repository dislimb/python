from django.shortcuts import render, redirect


from application.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')


def passcode(request):
    if request.POST['password'] == 'password':
        return render(request, 'dash.html')
    if request.POST['password'] == 'hard':
        return render(request, 'harddash.html')
    if request.POST['password'] != 'password':
        return redirect("https://www.youtube.com/watch?v=xvFZjo5PgG0")


def dash(request):
    return render(request, 'dash.html')

def snake(request):
    return render(request, 'snake.html')

def hardsnake(request):
    return render(request, 'hardsnake.html')