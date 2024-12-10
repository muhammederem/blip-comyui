from ..blip import Blip  # Import the BLIP model

class BlipProcessorNode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"multiline": False}),  # Input image
                "question": ("STRING", {"multiline": False, "default": "What is in the image?"}),  # Mandatory question
            },
            "optional": {
                **{
                    f"question_{i}": ("STRING", {"multiline": False, "default": ""})
                    for i in range(1, 10)  # Dynamically generate optional questions
                }
            },
        }

    RETURN_TYPES = ("LIST_STRING",)  # Output is a list of question-answer pairs and a list of answers
    FUNCTION = "process"
    OUTPUT_NODE = False  # Not a terminal node
    CATEGORY = "Blip"

    def process(self, image, question, **kwargs):
        """
        Process the image and questions, returning question-answer pairs.

        :param image: Input image.
        :param question: Mandatory question.
        :param kwargs: Optional questions (question_1 to question_9).
        :return: List of question-answer pairs as strings and list of answers as strings.
        """
        # Initialize BLIP model
        blip = Blip()

        # Gather all questions
        questions = [question]
        optional_questions = [kwargs[f"question_{i}"] for i in range(1, 10) if kwargs.get(f"question_{i}", "").strip()]
        questions.extend(optional_questions)

        # Limit to maximum of 10 questions
        questions = questions[:10]
        answers = []

        # Generate question-answer pairs
        for q in questions:
            answer = blip.ask(image, q)
            answers.append(answer)

        return (answers,)


