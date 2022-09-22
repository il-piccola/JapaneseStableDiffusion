from django.shortcuts import render, redirect

def index(request) :
    params = {
        'msg' : 'Hello World!',
    }
    return render(request, 'JapaneseStableDiffusion/index.html', params)

