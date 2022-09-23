import os
import torch
from torch import autocast
from diffusers import LMSDiscreteScheduler
from japanese_stable_diffusion import JapaneseStableDiffusionPipeline
from settings import *

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

print("HF_TOKEN", os.environ['HF_TOKEN'])

writeTest(TEST_PROCESS)

# Use the K-LMS scheduler here instead
scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)

pipe = JapaneseStableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16, scheduler=scheduler, use_auth_token=os.environ['HF_TOKEN'])
pipe = pipe.to(DEVICE)

with autocast(DEVICE):
    for imgfile in IMGLIST :
        image = pipe(readSentence(), guidance_scale=7.5)["sample"][0]
        save_path = os.path.join(STATIC_ROOT, imgfile)
        image.save(save_path)
        save_path2 = os.path.join(IMGDIR, imgfile)
        image.save(save_path2)

writeTest(TEST_FINISH)
