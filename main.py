from PIL import Image
from os import path
import sys

if len(sys.argv) == 2:
    try:
        im = Image.open(path.abspath(sys.argv[1]))
        px = im.load()
        setColor = set({})
        for x in range(im.width):
            for y in range(im.height):
                setColor.add(px[x, y])

        print(len(setColor))

    except FileNotFoundError:
        print("Unexpected error: file not found")
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[1])
        sys.exit(1)

else:
    print("usage: python3 pixel.py [FILE]\ne.g.: python3 pixel.py image.jpg")
