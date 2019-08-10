from unittest import TestCase
from unittest.mock import call, patch

import python4kyoani as py4ka


class TestMain(TestCase):
    @patch('sys.argv')
    @patch('python4kyoani.Path')
    @patch('python4kyoani.image.create_py4kaimage')
    @patch('python4kyoani.util.name_for_save')
    def test_normal_case(
            self, name_for_save, create_py4kaimage, path_init, mock_argv):
        image_path = path_init.return_value
        image_path.exists.return_value = True
        image = create_py4kaimage.return_value
        save_name = name_for_save.return_value

        py4ka.main()

        self.assertEqual(
            [call(mock_argv[1])], path_init.call_args_list)
        self.assertEqual([call(image_path)], create_py4kaimage.call_args_list)
        self.assertEqual(
            [call('PrayForKyoani')], image.write.call_args_list)
        self.assertEqual([call(image_path)], name_for_save.call_args_list)
        self.assertEqual([call(save_name)], image.save.call_args_list)
