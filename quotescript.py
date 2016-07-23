from PIL import Image, ImageFont, ImageDraw
import textwrap

quote = raw_input('Quote: ')
author = raw_input('Author: ')
position = raw_input('Position: ')
opinion = raw_input('Opinion? (y/n): ') in ['y', 'yes', 'YES', 'Y', 'Yes', '1']

quotetext_font = ImageFont.truetype("suecaslab-light.otf", 60)
authortext_font = ImageFont.truetype("suecaslab-heavy.otf", 60)
titletext_font = ImageFont.truetype("suecaslab-light.otf", 45)
opinion_font = ImageFont.truetype("suecaslab-semibold.otf", 60)
thc_op_font = ImageFont.truetype("bigmoore.otf", 18)
thc_font = ImageFont.truetype("bigmoore.otf", 36)

breakquote = textwrap.wrap(quote, width=35)

img = None
if opinion:
    img = Image.new('RGB', (1120, 600), "#a82931")
    draw = ImageDraw.Draw(img)
    counter = 0
    for line in breakquote:
        draw.text((28,50 + (counter * 60)), line, font=quotetext_font, fill=(255,255,255,255))
        counter += 1
    draw.text((28, 420), author, font=authortext_font, fill=(255,255,255,255))
    draw.text((28, 490), position, font=titletext_font, fill=(255,255,255,255))
        
    draw.text((860, 510), "opinion", font=opinion_font, fill=(255,255,255,255))
    draw.text((922, 570), "The Harvard Crimson", font=thc_op_font, fill=(255,255,255,255))
    draw = ImageDraw.Draw(img)
else:
    seal = Image.open("seal-trans-sm.png")
    img = Image.new('RGB', (1120,600), "white")
    img.paste(seal, (800, 250), seal)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0,0), (1120, 30)], "#a82931")
    counter = 0
    for line in breakquote:
        draw.text((28,50 + (counter * 60)), line, font=quotetext_font, fill="#a82931")
        draw.text((28, 420), author, font=authortext_font, fill="#a82931")
        draw.text((28, 490), position, font=titletext_font, fill="#a82931")
        draw.text((775, 550), "The Harvard Crimson", font=thc_font, fill="#a82931")
        counter += 1
    draw = ImageDraw.Draw(img)

img.show()
