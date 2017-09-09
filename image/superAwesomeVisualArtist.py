from PIL import Image, ImageFilter

im = Image.open('a.jpg')
sly = Image.open('unknown.jpeg')

x = im.resize((128, 128))
y = sly.resize((128, 128))
y.show()
z = Image.blend(x, y, 0.4)
z.show()

 



