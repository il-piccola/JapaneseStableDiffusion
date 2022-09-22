from subprocess import run, Popen, PIPE
from django.shortcuts import render, redirect
from .settings import *

def index(request) :
    params = {
        'title' : 'Japanese Stable Diffusion Test',
        'prompt' : '画像生成実行中...',
        'reload' : True,
    }
    s = isRunningTest()
    if s == "" :
        runTest()
    elif s == TEST_FINISH :
        with open(TEST_TXT, mode="w") as f :
            f.write("")
        params['prompt'] = PROMPT
        params['img'] = IMGFILE
        params['reload'] = False
    return render(request, 'JapaneseStableDiffusion/index.html', params)

def runTest() :
    proc = Popen(TEST_COM, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    return

def isRunningTest() :
    s = ""
    with open(TEST_TXT) as f :
        s = f.read()
    return s
