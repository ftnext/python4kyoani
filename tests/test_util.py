from pathlib import Path
from unittest import TestCase

import python4kyoani.util as u


class TestNameForSave(TestCase):
    def test_same_dir(self):
        path = Path('current_dir.png')
        actual = u.name_for_save(path)
        self.assertEqual('pray_current_dir.png', actual)

    def test_another_dir(self):
        path = Path('../another_dir/image.jpg')
        actual = u.name_for_save(path)
        self.assertEqual('pray_image.jpg', actual)
