from PIL import Image


def resize(image):
    img = Image.open(image)
    img = img.resize((350, 350), Image.ANTIALIAS)
    img.save(image)
