import torch
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering
import time

class Blip:
    # Class variables for singleton pattern
    _instance = None
    _initialized = False

    def __new__(cls):
        # Ensure only one instance is created (singleton pattern)
        if cls._instance is None:
            cls._instance = super(Blip, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize the model only once
        if not Blip._initialized:
            # Load BLIP processor for image and text processing
            self.processor = BlipProcessor.from_pretrained("ybelkada/blip-vqa-base")
            # Load BLIP model with float16 precision on GPU
            self.model = BlipForQuestionAnswering.from_pretrained(
                "ybelkada/blip-vqa-base", 
                torch_dtype=torch.float16
            ).to("cuda")
            Blip._initialized = True

    def ask(self, image_path, question):
        # Load and convert image to RGB
        raw_image = Image.open(image_path).convert('RGB')
        # Process image and question into model inputs
        inputs = self.processor(
            raw_image, 
            question, 
            return_tensors="pt"
        ).to("cuda", torch.float16)
        
        # Generate answer using the model
        out = self.model.generate(**inputs)
        # Decode and return the answer
        return self.processor.decode(out[0], skip_special_tokens=True)
    
# #test the model with more than one question and image and chech the time taken to answer the question and caching 
# image_path = "/home/erem/Documents/muhammet-faruk-erem/blip-comyui/car.webp"
# questions = [
#     "What is the color of the car?",
#     "How many cars are in the image?",
#     "What is the model of the car?"
# ]
# s = time.time()
# blip1 = Blip()
# print("time taken to initialize the model: ", time.time() - s)
# s = time.time()
# blip2 = Blip()
# print("time taken to initialize the model: ", time.time() - s)
# s = time.time()
# blip3 = Blip()
# print("time taken to initialize the model: ", time.time() - s)
# for question in questions:
#     s = time.time()
#     blip = Blip()
#     print(blip.ask(image_path, question))
#     print(f"Time taken: {time.time() - s:.2f} seconds")