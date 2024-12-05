from .services.blip import Blip


class BlipNode:

    @classmethod
    def INPUT_TYPES(cls):
        return { "required" : {
            "image_path": ("image", {"multiline": False, "default": "image.jpg"}),
            "question": ("STRING", {"multiline": False, "default": "image.jpg"})
        },
        "optional": {
            "question-2": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question-3": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question-4": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question-5": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question-6": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question-7": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question-8": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question-9": ("STRING", {"multiline": False, "default": "image.jpg"}),
            "question-10": ("STRING", {"multiline": False, "default": "image.jpg"})        }
        }

    RETURN_TYPES = ("LIST")
    FUCNTION = "process"
    OUTPUT_NODE = "True"
    CATEGORY = "Blip"

    def process(self, image_path, question, question_2=None, question_3=None, question_4=None, 
                question_5=None, question_6=None, question_7=None, question_8=None, 
                question_9=None, question_10=None):
        blip = Blip()
        answers = [blip.ask(image_path, question)]
        
        optional_questions = [question_2, question_3, question_4, question_5,
                            question_6, question_7, question_8, question_9, question_10]
        
        for q in optional_questions:
            if q:  # Only process if question is not None or empty
                answers.append(blip.ask(image_path, q))
                
        return answers

