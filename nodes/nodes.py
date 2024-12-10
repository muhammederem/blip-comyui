from ..blip import Blip  # Import the BLIP model
import torchvision.transforms.functional as F

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

        :param image: Input image tensor (B,C,H,W).
        :param question: Mandatory question.
        :param kwargs: Optional questions (question_1 to question_9).
        :return: List of answers as strings.
        """
        # Convert first image in batch to PIL
        if len(image.shape) == 4:
            image = image[0]
        
        # Check number of channels
        if image.shape[0] not in [1, 3]:
            # If channels are last dimension, permute them
            if image.shape[-1] in [1, 3]:
                image = image.permute(2, 0, 1)
            else:
                raise ValueError(f"Image must have 1 or 3 channels, got {image.shape[0]} channels")
    
        # Ensure 3D tensor (C,H,W)
        if len(image.shape) != 3:
            raise ValueError(f"Image tensor must be 3D (C,H,W), got shape {image.shape}")
            
        # Convert to PIL image
        pil_image = F.to_pil_image(image, mode='RGB' if image.shape[0] == 3 else 'L')
        
        # Initialize BLIP model
        blip = Blip()

        # Rest of the code remains same...
        questions = [question]
        optional_questions = [kwargs[f"question_{i}"] for i in range(1, 10) if kwargs.get(f"question_{i}", "").strip()]
        questions.extend(optional_questions)

        questions = questions[:10]
        answers = []

        for q in questions:
            answer = blip.ask(pil_image, q)
            answers.append(answer)
            print(f"Q: {q}\nA: {answer}")

        return (answers,)


class ListToTextNode:
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list": ("LIST_STRING", {"multiline": True}),  # List of strings
            },
            "optional": {},
        }
    
    RETURN_TYPES = ("STRING",)  # Output is a single string
    FUNCTION = "process"
    OUTPUT_NODE = True  # Terminal node
    CATEGORY = "Blip"

    def process(self, list, **kwargs):
        """
        Convert a list of strings to a single text.

        :param list: List of strings.
        :param kwargs: Optional arguments.
        :return: Single text.
        """
        print(f"List: {list}")
        return "\n".join(list)

