from PIL import Image, ImageFont, ImageDraw
import textwrap

#1200 x 627 for Facebook
#400 x 220 for Twitter
#1120 x 600

quote = raw_input('Quote: ')
author = raw_input('Author: ')
position = raw_input('Position: ')
opinion = raw_input('Opinion? (y/n): ') in ['y', 'yes', 'YES', 'Y', 'Yes', '1']


img = Image.new('RGB', (1120, 600), "#a82931")
quotetext_font = ImageFont.truetype("suecaslab-light.otf", 60)
authortext_font = ImageFont.truetype("suecaslab-heavy.otf", 60)
titletext_font = ImageFont.truetype("suecaslab-light.otf", 63)
opinion_font = ImageFont.truetype("suecaslab-semibold.otf", 55)
thc_font = ImageFont.truetype("bigmoore.otf", 18)

breakquote = textwrap.wrap(quote, width=35)

draw = ImageDraw.Draw(img)

counter = 0
for line in breakquote:
    draw.text((28,50 + (counter * 60)), line, font=quotetext_font)
    counter += 1
    
draw.text((28, 420), author, font=authortext_font)
draw.text((28, 490), position, font=titletext_font)

if opinion:
    draw.text((900, 490), "opinion", font=opinion_font)
    draw.text((910, 530), "The Harvard Crimson", font=thc_font)


draw = ImageDraw.Draw(img)

img.show()
