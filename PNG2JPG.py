import os
from PIL import Image

def convert_image(image_path):
    try:
        image = Image.open(image_path)
        if image.format != 'JPEG':
            output_path = os.path.splitext(image_path)[0]+".jpg"
            image = image.convert('RGB')
            image.save(output_path, "JPEG")
            print(f"conversion successful, image saved as {output_path}")
        else:
            print("Image is already in JPEG formate")

    except OSError as e:
        print(f"conversion is failed dude to {e} of file {image_path}")

image_path = 'Im2.png'
convert_image(image_path)