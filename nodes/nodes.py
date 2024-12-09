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

    RETURN_TYPES = ("LIST_STRING",)  # Output is a list of question-answer pairs
    FUNCTION = "process"
    OUTPUT_NODE = False  # Not a terminal node
    CATEGORY = "Blip"

    def process(self, image, question, **kwargs):
        """
        Process the image and questions, returning question-answer pairs.

        :param image: Input image.
        :param question: Mandatory question.
        :param kwargs: Optional questions (question_1 to question_9).
        :return: List of question-answer pairs as strings.
        """
        # Initialize BLIP model
        blip = Blip()

        # Gather all questions
        questions = [question]
        optional_questions = [kwargs[f"question_{i}"] for i in range(1, 10) if kwargs.get(f"question_{i}", "").strip()]
        questions.extend(optional_questions)

        # Limit to maximum of 10 questions
        questions = questions[:10]

        # Generate question-answer pairs
        question_answer_pairs = []
        for q in questions:
            answer = blip.ask(image, q)
            question_answer_pairs.append(f"Q: {q}\nA: {answer}")
        print(question_answer_pairs)

        return (question_answer_pairs,)


class BlipDisplayNode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"multiline": False}),  # Input image
                "qa_pairs": ("LIST_STRING", {"multiline": True}),  # Question-answer pairs from the processor node
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")  # Output includes the image and formatted QA text
    FUNCTION = "process"
    OUTPUT_NODE = True  # Terminal node
    CATEGORY = "Blip"

    def process(self, image, qa_pairs):
        """
        Display the image and formatted QA pairs.

        :param image: Input image.
        :param qa_pairs: List of question-answer pairs.
        :return: The image and formatted text for visualization.
        """
        # Format the question-answer pairs as a single string for display
        formatted_output = "\n\n".join(qa_pairs)

        return image, formatted_output


class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "Blip"

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = [text]

        return {"ui": {"text": text}, "result": (text,)}