from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch
import streamlit as st


@st.cache_resource
def load_blip2():
    #Load and cache the BLIP-2 model and processor

    processor = Blip2Processor.from_pretrained("salesforce/blip2-opt-2.7b")
    model = Blip2ForConditionalGeneration.from_pretrained("salesforce/blip2-opt-2.7b", torch_dtype=torch.float16 )

    # Use GPU when CUDA is available otherwise use CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    return processor, model, device


def createimagecaption(image):
    #Generate a caption for the given image using BLIP-2

    processor, model, device = load_blip2()
    inputs = processor(images=image, return_tensors="pt" ).to(device, torch.float16)
    generated_ids = model.generate(**inputs,max_new_tokens=20)
    caption = processor.batch_decode(generated_ids, skip_special_tokens=True )[0].strip()

    return caption

