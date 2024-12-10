from blip import Blip
from PIL import Image
import argparse

def test_blip_with_questions(blip=None, image_path1="image1.webp", image_path2="images.jpeg", questions1=None, questions2=None):
    if blip is None:
        blip = Blip()

    try:
        image = Image.open(image_path1)
    except Exception as e:
        print(f"Error opening image {image_path1}: {e}")
        return

    try:
        image2 = Image.open(image_path2)
    except Exception as e:
        print(f"Error opening image {image_path2}: {e}")
        return

    for q in questions1:
        try:
            print(f"Q: {q}\nA: {blip.ask(image, q)}")
        except Exception as e:
            print(f"Error processing question '{q}' for image {image_path1}: {e}")

    for q in questions2:
        try:
            print(f"Q: {q}\nA: {blip.ask(image2, q)}")
        except Exception as e:
            print(f"Error processing question '{q}' for image {image_path2}: {e}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Test BLIP with questions on images.")
    parser.add_argument("--image_path1", type=str, default="image1.webp", help="Path to the first image.")
    parser.add_argument("--image_path2", type=str, default="images.jpeg", help="Path to the second image.")
    parser.add_argument("--questions1", nargs='+', default=["What are those in the image?", "How many cars in there?", "Is there blue car in the image?"], help="List of questions for the first image.")
    parser.add_argument("--questions2", nargs='+', default=["Is he wearing sunglasses", "How many people in the image?", "What is the man wearing?"], help="List of questions for the second image.")
    
    args = parser.parse_args()

    test_blip_with_questions(image_path1=args.image_path1, image_path2=args.image_path2, questions1=args.questions1, questions2=args.questions2)
