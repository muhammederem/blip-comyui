import torch
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

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

    def ask(self, image, question):
        # Load and convert image to RGB
        raw_image = image
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
