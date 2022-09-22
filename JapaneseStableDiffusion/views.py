import os
from subprocess import Popen, PIPE
from django.shortcuts import render, redirect
from .settings import *

def index(request) :
    params = {
        'title' : 'Japanese Stable Diffusion Test',
        'prompt' : '画像生成実行中...',
        'reload' : False,
    }
    s = readTest()
    if s == "" :
        if request.POST :
            writeSentence(request.POST['sentence'])
            Popen(TEST_COM, shell=True, stdout=PIPE, stderr=PIPE, text=True)
            params['reload'] = True
    elif s == TEST_PROCESS :
        params['reload'] = True
    elif s == TEST_FINISH :
        writeTest("")
        params['prompt'] = '画像生成完了'
        params['img'] = IMGFILE
    return render(request, 'JapaneseStableDiffusion/index.html', params)

def readTest() :
    s = ""
    if os.path.exists(TEST_TXT) :
        with open(TEST_TXT) as f :
            s = f.read()
    return s

def writeTest(s) :
    with open(TEST_TXT, mode="w") as f :
        f.write(s)
    return

def readSentence() :
    s = ""
    if os.path.exists(SENTENCE_FILE) :
        with open(SENTENCE_FILE) as f :
            s = f.read()
    return s

def writeSentence(s) :
    with open(SENTENCE_FILE, mode="w") as f :
        f.write(s)
    return
