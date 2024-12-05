from ..blip import Blip


class BlipNode:

    @classmethod
    def INPUT_TYPES(cls):
        return { "required" : {
            "image_path": ("IMAGE", {"multiline": False, "default": "image.jpg"}),
            "question": ("STRING", {"multiline": False, "default": "image.jpg"})
        },
        "optional": 
        {"question_1": ("STRING", {"multiline": False, "default": "image.jpg"}),
         "question_2": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question_3": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question_4": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question_5": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question_6": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question_7": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question_8": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question_9": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question_10": ("STRING", {"multiline": False, "default": "image.jpg"}),
       }}


    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    OUTPUT_NODE = True
    CATEGORY = "Blip"

    def process(self, image_path, question, question_1=None, question_2=None, question_3=None, question_4=None, question_5=None, question_6=None, question_7=None, question_8=None, question_9=None, question_10=None):
        blip = Blip()
        answers = blip.ask(image_path, question)
        
        optional_questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]
        for q in optional_questions:
            if q:
                answers += blip.ask(image_path, q)
        
        return (answers)

