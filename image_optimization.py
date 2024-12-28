import PIL.Image as Image
import PIL.ImageFilter as ImageFilter
import PIL.ImageOps as ImageOps
import PIL.ImageEnhance as ImageEnhance

def crop_image(image, start_x, start_y, end_x, end_y):
    return image.crop((start_x, start_y, end_x, end_y))

def resize_image(image, width, height):
    return image.resize((width, height))

def flip_image(image):
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

def rotate_image(image, degrees):
    return image.rotate(degrees)

def compress_image(image, save_path, quality=85):
    if not (1 <= quality <= 100):
        raise ValueError("Quality must be between 1 and 100.")
    image.save(save_path, optimize=True, quality=quality)

def blur_image(image):
    return image.filter(ImageFilter.BLUR)

def sharp_image(image):
    return image.filter(ImageFilter.SHARPEN)

def adjust_brightness(image, brightness):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(brightness)

def adjust_contrast(image, contrast):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(contrast)

def add_filter(image):
    image = ImageOps.grayscale(image)
    image = ImageOps.invert(image)
    image = ImageOps.posterize(image, 4)
    return image

def optimize_image(image):
    image = resize_image(image, 100, 100)
    return image

try:
    im = Image.open("image2.jpg")
    optimized_image = optimize_image(im)
    optimized_image.save("resize.png")
    print("Image optimized and saved successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
