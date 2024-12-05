from ..blip import Blip


class BlipNode:

    @classmethod
    def INPUT_TYPES(cls):
        return { "required" : {
            "image_path": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question": ("STRING", {"multiline": False, "default": "image.jpg"})
        },
       }


    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    OUTPUT_NODE = True
    CATEGORY = "Blip"

    def process(self, image_path, question):
        blip = Blip()
        answers = blip.ask(image_path, question)
        
        return (answers)

