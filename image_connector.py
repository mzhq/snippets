import os
from PIL import Image

path = 'F:/station/connector/fig'
rows = 2
cols = 2

image_names = os.listdir(path)
image_names.sort(key = lambda x: int(x[:-4]))
print(image_names)

images = [Image.open(path + '/' + name) for name in image_names]
unit_width = images[0].width
unit_height = images[0].height
big_image = Image.new('RGB', (unit_width * cols, unit_height * rows))

for r in range(rows):
    for c in range(cols):
        img = images[r * cols + c].resize((unit_width, unit_height))
        big_image.paste(img, (unit_width * c, unit_height * r))

big_image.save(path + '/result.bmp')





