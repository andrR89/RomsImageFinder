from PIL import Image


def resize(image):
    try:
        img = Image.open(image)
        img = img.resize((300, 200), Image.ANTIALIAS)
        img.save(image)
    except Exception:
        print("Nao foi possivel mudar : "+ image)
