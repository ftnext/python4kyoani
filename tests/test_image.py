from unittest import TestCase
from unittest.mock import MagicMock, patch

import python4kyoani.image as i


class TestCreatePy4kaimage(TestCase):
    @patch('python4kyoani.image.Image.open')
    def test(self, image_open):
        img_path = MagicMock()

        img = i.create_py4kaimage(img_path)

        self.assertIsInstance(img, i.Py4kaImage)
        self.assertEqual(img.image, image_open.return_value)
