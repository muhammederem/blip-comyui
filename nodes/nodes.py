from ..blip import Blip

class BlipNode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "blip_model": ("STRING", {"multiline": False, "default": "blip_base"}),  # Model selector
                "image": ("IMAGE", {"multiline": False}),  # Image input directly
                "question": ("STRING", {"multiline": False, "default": "What is in the image?"}),
            },
            "optional": {
                "additional_questions": ("STRING_LIST", {"multiline": True, "default": []}),  # List of additional questions
            },
        }

    RETURN_TYPES = ("LIST_STRING",)
    FUNCTION = "process"
    OUTPUT_NODE = True
    CATEGORY = "Blip"

    def process(self, blip_model, image, question, additional_questions=None):
        """
        Process the image with the BLIP model and answer the questions.

        :param blip_model: Name of the BLIP model to use (e.g., "blip_base").
        :param image: The image input (as binary or object).
        :param question: The primary question to ask.
        :param additional_questions: A list of additional questions (optional).
        :return: A list of answers (strings).
        """
        # Initialize the selected BLIP model
        blip = Blip(model_name=blip_model)

        # Answer the primary question
        answers = [blip.ask(image, question)]

        # Process additional questions if provided
        if additional_questions:
            for q in additional_questions:
                if q.strip():  # Skip empty questions
                    answers.append(blip.ask(image, q.strip()))

        return answers
