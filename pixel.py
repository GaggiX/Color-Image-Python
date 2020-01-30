from PIL import Image
from sys import argv
from os import path

im = Image.open(path.abspath(argv[1]))
px = im.load()
setColor = set({})
for x in range(im.width):
    for y in range(im.height):
        setColor.add(px[x, y])

print(len(setColor))
