from PIL import Image


class Py4kaImage:
    def __init__(self, image_path):
        self.image = Image.open(image_path)


def create_py4kaimage(image_path):
    return Py4kaImage(image_path)
