from ..blip import Blip  # Import the BLIP model

class BlipCustomNode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"multiline": False}),  # Required image input
                "question": ("STRING", {"multiline": False, "default": "What is in the image?"}),  # Required main question
            },
            "optional": {
                "question_1": ("STRING", {"multiline": False, "default": ""}),
                "question_2": ("STRING", {"multiline": False, "default": ""}),
                "question_3": ("STRING", {"multiline": False, "default": ""}),
                "question_4": ("STRING", {"multiline": False, "default": ""}),
                "question_5": ("STRING", {"multiline": False, "default": ""}),
                "question_6": ("STRING", {"multiline": False, "default": ""}),
                "question_7": ("STRING", {"multiline": False, "default": ""}),
                "question_8": ("STRING", {"multiline": False, "default": ""}),
                "question_9": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("LIST_STRING",)  # Return a list of answers as strings
    FUNCTION = "process"
    OUTPUT_NODE = True
    CATEGORY = "Blip"

    def process(self, image, question, question_1=None, question_2=None, question_3=None, question_4=None,
                question_5=None, question_6=None, question_7=None, question_8=None, question_9=None):
        """
        Process the image with the BLIP model and answer the questions.

        :param image: Input image (provided by ComfyUI).
        :param question: The main required question to ask.
        :param question_1 to question_9: Optional additional questions (maximum 9).
        :return: A list of answers to all provided questions.
        """
        # Initialize the BLIP model (GPU or CPU usage can be adjusted inside the model)
        blip = Blip()

        # Collect all questions, starting with the required one
        questions = [question]  # Include the mandatory question
        optional_questions = [question_1, question_2, question_3, question_4, question_5, 
                              question_6, question_7, question_8, question_9]

        # Add non-empty optional questions to the list
        for q in optional_questions:
            if q and q.strip():  # Ignore empty or whitespace-only questions
                questions.append(q.strip())

        # Ensure the total question count does not exceed 10
        if len(questions) > 10:
            questions = questions[:10]

        # Answer each question using the BLIP model
        answers = [blip.ask(image, q) for q in questions]

        return answers  # Return the list of answers
