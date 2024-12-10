from blip import Blip
from PIL import Image
import argparse

def test_blip_with_questions(blip=None, image_path="image1.webp", questions=None):
    """
    Test the BLIP model with a set of questions for an image.

    Args:
        blip (Blip, optional): An instance of the Blip model. If None, a new instance will be created. 
        image_path (str, optional): The file path to the image. Defaults to "image1.webp".
        questions (list of str, optional): A list of questions to ask about the image.

    Example:
        test_blip_with_questions(
            blip=my_blip_instance,
            image_path="path/to/image.jpg",
            questions=["What is in the image?", "What color is the object?"]
        )
    """
    if blip is None:
        blip = Blip()

    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image {image_path}: {e}")
        return

    for q in questions:
        try:
            print(f"Q: {q}\nA: {blip.ask(image, q)}")
        except Exception as e:
            print(f"Error processing question '{q}' for image {image_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test BLIP with questions on an image.")
    parser.add_argument("--image_path", type=str, default="image1.webp", 
                       help="Path to the image.")
    parser.add_argument("--questions", nargs='+', 
                       default=["What are those in the image?", 
                               "How many cars in there?", 
                               "Is there blue car in the image?"], 
                       help="List of questions for the image.")
    
    args = parser.parse_args()
    test_blip_with_questions(image_path=args.image_path, questions=args.questions)
