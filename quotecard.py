from PIL import Image, ImageFont, ImageDraw
import textwrap

#1200 x 627 for Facebook
#400 x 220 for Twitter
#1120 x 600

quote = raw_input('Input Quote: ')

author = "DKC"
img = Image.new('RGB', (1120, 600), "#a82931")
sueca_light = ImageFont.truetype("suecaslab-light.otf", 24)

draw = ImageDraw.Draw(img)
draw.text((0,0), quote, font=sueca_light)
draw = ImageDraw.Draw(img)

img.show()
