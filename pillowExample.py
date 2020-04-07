#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pc
#
# Created:     07/04/2020
# Copyright:   (c) pc 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PIL import Image, ImageDraw, ImageFont

f=open('guestsFile.txt','r')

for line in f:
    print(line)
    #Creating a new Image ith white background
    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)
    for i in range(100, 200, 10):
       draw.line([(i, 0), (200, i - 100)], fill='red')
    draw.text((50, 100), "Welome!", fill='Pink')
    draw.ellipse((-20,140, 168, 168), fill='purple')
    draw.text((35, 150), line, fill='white')
    sv = line.rstrip()+".png"
    im.save(sv)
