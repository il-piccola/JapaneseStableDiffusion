from subprocess import run, Popen, PIPE
from django.shortcuts import render, redirect
from .settings import *

def index(request) :
    params = {
        'title' : 'Japanese Stable Diffusion Test',
        'prompt' : '画像生成実行中...',
        'reload' : True,
    }
    s = readTest()
    if s == "" :
        proc = Popen(TEST_COM, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    elif s == TEST_FINISH :
        writeTest("")
        params['prompt'] = PROMPT
        params['img'] = IMGFILE
        params['reload'] = False
    return render(request, 'JapaneseStableDiffusion/index.html', params)

def readTest() :
    s = ""
    with open(TEST_TXT) as f :
        s = f.read()
    return s

def writeTest(s) :
    with open(TEST_TXT, mode="w") as f :
        f.write(s)
    return
