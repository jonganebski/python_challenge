# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image
image = Image.open('oxygen.png')
print(image.size)
# im = image.load()
im_rgb = image.convert('RGB')
(width, height) = image.size

for h in range(height):
    same_rgb = []
    for w in range(width):
        rgb = im_rgb.getpixel((w, h))
        if rgb[0] == rgb[1] == rgb[2]:
            same_rgb.append(rgb)
    print(same_rgb)

# for i in range(0, width):

