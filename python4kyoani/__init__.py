from pathlib import Path
import sys

import python4kyoani.image as i


def main():
    image_path = Path(sys.argv[1])
    if not image_path.exists():
        print('指定されたファイルパスが正しくないようです')
        return
    image = i.create_py4kaimage(image_path)
    image.write('PrayForKyoani')
    image.save(image_path)
