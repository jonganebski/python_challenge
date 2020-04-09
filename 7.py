from PIL import Image

image = Image.open('oxygen.png')
print(image.size)
# im = image.load()
im_rgb = image.convert('RGB')
(width, height) = image.size

# for h in range(height):
#     same_rgb = []
#     for w in range(width):
#         rgb = im_rgb.getpixel((w, h))
#         if rgb[0] == rgb[1] == rgb[2]:
#             same_rgb.append(rgb)
#             print(w, h)
# (0, 43) ~ (607, 51)
# for i in range(0, width):

answer = ''
for i in range(width):
    rgb = im_rgb.getpixel((i, 43))
    if rgb[0] == rgb[1] == rgb[2]:
        if i >= 1 and answer[-1] == chr(rgb[0]):
            None
        else:
            answer += (chr(rgb[0]))
print(answer)
