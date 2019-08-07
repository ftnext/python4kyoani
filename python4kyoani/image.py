from PIL import Image, ImageDraw


class Py4kaImage:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.draw = None

    def _start_coordinate_of_text(self, message):
        width, height = self.image.size
        font_size = round(0.1*height)
        # 日本語では1文字あたりfont_size × font_sizeの正方形と想定できるが、
        # アルファベットは縦方向に長いので、0.5をかけることにする
        message_length = 0.5 * font_size * len(message)
        x_coordinate = round((width - message_length)/2)
        y_coordinate = round((height-font_size)/2)
        return x_coordinate, y_coordinate

    def write(self, message):
        if self.draw is None:
            self.draw = ImageDraw.Draw(self.image)
        start_coordinate = self._start_coordinate_of_text(message)
        self.draw.text(start_coordinate, message, fill='gray')

    def save(self, save_name):
        self.image.save(save_name)


def create_py4kaimage(image_path):
    return Py4kaImage(image_path)
