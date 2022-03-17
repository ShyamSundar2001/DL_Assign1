from PIL import Image
from PIL import ImageOps

for i in range(16,19):
	im = Image.open("2.1.{}.png".format(i+1))

	fill_color = (255,255,255)  # your new background color

	im = im.convert("RGBA")   # it had mode P after DL it from OP
	if im.mode in ('RGBA', 'LA'):
	    background = Image.new(im.mode[:-1], im.size, fill_color)
	    background.paste(im, im.split()[-1]) # omit transparency
	    im = background


	im = im.convert("RGB")
	im = ImageOps.crop(im,(150,50,100,100))
	im.save("2.1.{}.png".format(i+1))