from unittest import TestCase
from unittest.mock import call, MagicMock, patch

import python4kyoani.image as i


class TestCreatePy4kaimage(TestCase):
    @patch('python4kyoani.image.Image.open')
    def test(self, image_open):
        img_path = MagicMock()

        img = i.create_py4kaimage(img_path)

        self.assertIsInstance(img, i.Py4kaImage)
        self.assertEqual(img.image, image_open.return_value)
        self.assertIsNone(img.draw)


class TestPy4kaImageWrite(TestCase):
    @patch('python4kyoani.image.Image.open')
    @patch('python4kyoani.image.ImageDraw.Draw')
    @patch('python4kyoani.image.Py4kaImage._start_coordinate_of_text')
    def test_draw_not_set(
            self, start_coordinate_of_text, image_draw_draw, mock_open):
        draw = image_draw_draw.return_value
        start_coordinate = start_coordinate_of_text.return_value

        image_path = MagicMock()
        img = i.Py4kaImage(image_path)
        img.draw = None
        message = MagicMock()
        img.write(message)

        self.assertEqual([call(img.image)], image_draw_draw.call_args_list)
        self.assertEqual(
            [call(message)], start_coordinate_of_text.call_args_list)
        self.assertEqual(
            [call(start_coordinate, message, fill='gray')],
            draw.text.call_args_list)
        self.assertEqual(draw, img.draw)

    @patch('python4kyoani.image.Image.open')
    @patch('python4kyoani.image.Py4kaImage._start_coordinate_of_text')
    def test_draw_set(self, start_coordinate_of_text, mock_open):
        start_coordinate = start_coordinate_of_text.return_value

        image_path = MagicMock()
        img = i.Py4kaImage(image_path)
        message = MagicMock()
        img.write(message)

        self.assertEqual(
            [call(message)], start_coordinate_of_text.call_args_list)
        self.assertEqual(
            [call(start_coordinate, message, fill='gray')],
            img.draw.text.call_args_list)
