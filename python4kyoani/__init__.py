from pathlib import Path
import sys

import python4kyoani.image as i
import python4kyoani.util as u


def main():
    image_path = Path(sys.argv[1])
    if not image_path.exists():
        print('指定されたファイルパスが正しくないようです')
        return
    image = i.create_py4kaimage(image_path)
    image.write('PrayForKyoani')
    save_name = u.name_for_save(image_path)
    image.save(save_name)
