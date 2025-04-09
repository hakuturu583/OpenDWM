from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-3.5-medium", cache_dir="./stable-diffusion-3.5-medium")