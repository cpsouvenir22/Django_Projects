from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime

def showtime (request):
    return redirect('/time_display')


def whatTimeIsIt (request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)