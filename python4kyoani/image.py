from PIL import Image, ImageDraw


class Py4kaImage:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.draw = None

    def _start_coordinate_of_text(self, message):
        raise NotImplementedError

    def write(self, message):
        if self.draw is None:
            self.draw = ImageDraw.Draw(self.image)
        start_coordinate = self._start_coordinate_of_text(message)
        self.draw.text(start_coordinate, message, fill='gray')


def create_py4kaimage(image_path):
    return Py4kaImage(image_path)
