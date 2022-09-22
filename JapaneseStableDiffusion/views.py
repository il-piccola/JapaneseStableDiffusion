from subprocess import run, Popen, PIPE
from django.shortcuts import render, redirect
from .settings import *

def index(request) :
    params = {
        'title' : 'Japanese Stable Diffusion Test',
        'prompt' : PROMPT,
        'imgfile' : IMGFILE,
    }
    proc = run(TEST_COM, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    return render(request, 'JapaneseStableDiffusion/index.html', params)

