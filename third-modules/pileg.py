#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import Image;

# im = Image.open('./0.jpg');
# w, h = im.size;
# im.thumbnail((w/2, h/2));
# im.save('./thumbnail.jpg', 'jpeg');

#########################################################################
import Image, ImageDraw, ImageFont, ImageFilter;
import random;

def rndChar():
    return chr(random.randint(65, 90));

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255));

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127));

width = 160 * 4;
height = 160;
image = Image.new('RGB', (width, height), (255, 255, 255));

font = ImageFont.truetype('/usr/share/fonts/truetype/openoffice/opens___.ttf', 100);

draw = ImageDraw.Draw(image);

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor());

for t in range(4):
    draw.text((160 * t + 30, 30), rndChar(), font = font, fill = rndColor2());

image = image.filter(ImageFilter.BLUR);
image.save('code.jpg', 'jpeg');

