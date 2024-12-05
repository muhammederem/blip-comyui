import numpy as np
import torch
from blip import Blip


       
class PrintHelloWorld:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "image_path": ("STRING", {"multiline": False, "default": "Hello World"}),
                    }
                }

    RETURN_TYPES = ()
    FUNCTION = "print_text"
    OUTPUT_NODE = True
    CATEGORY = "🧩 Tutorial Nodes"

    def print_text(self, text):

        print(f"Tutorial Text : {text}")
        
        return {}

    def process(self, image_path, question="What is the color of dog?"):
        blip = Blip()
        answers =blip.ask(image_path, question)
        
        return answers

