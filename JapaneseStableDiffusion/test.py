import torch
from torch import autocast
from diffusers import LMSDiscreteScheduler
from japanese_stable_diffusion import JapaneseStableDiffusionPipeline

MODEL_ID = "rinna/japanese-stable-diffusion"
DEVICE = "cuda"
YOUR_TOKEN = "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"
PROMPT = "蒼い空と青い海"
 
# Use the K-LMS scheduler here instead
scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
 
pipe = JapaneseStableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16, scheduler=scheduler, use_auth_token=YOUR_TOKEN)
pipe = pipe.to(DEVICE)
 
with autocast(DEVICE):
    image = pipe(PROMPT, guidance_scale=7.5)["sample"][0]
 
image.save("output.png")
