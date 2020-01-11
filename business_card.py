#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in9b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd2in9b.EPD()
    epd.init()
    print("clear")
    epd.Clear(0xFF)
    
    # Drawing on the Horizontal image
    Blackimage = Image.new('1', (epd2in9b.EPD_HEIGHT, epd2in9b.EPD_WIDTH), 255)  # 298*126
    Redimage = Image.new('1', (epd2in9b.EPD_HEIGHT, epd2in9b.EPD_WIDTH), 255)  # 298*126    

    BSU = Image.open('/path/to/small_84x69.bmp')
    AU = Image.open('/path/to/small_42x41.bmp')

    Redimage.paste(BSU, (0,0))
    Redimage.paste(AU, (250, 85))
    
    # Horizontal
    print("Drawing")
    drawblack = ImageDraw.Draw(Blackimage)
    drawred = ImageDraw.Draw(Redimage)
    font22o = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf', 22)
    font16 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
    font12 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
    font14 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    font14o = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf', 14)
    drawblack.text((90, 0), 'Larry A. Hartman', font = font22o, fill = 0)
    drawblack.text((90, 32), 'email@address', font = font12, fill = 0)
    drawblack.text((90, 48), '(xxx) xxx-xxxx', font = font12, fill = 0)
    drawred.line((0, 80, epd2in9b.EPD_HEIGHT, 80), fill = 0)
    drawblack.text((10, 86), 'Beginning of short prose', font = font14o, fill = 0)
    drawblack.text((10, 102), 'End of short prose', font = font14o, fill = 0)
    drawblack.text((170, 102), 'Reference', font = font14, fill = 0)
    # drawred.line((140, 75, 190, 75), fill = 0)
    # drawred.arc((140, 50, 190, 100), 0, 360, fill = 0)
    # drawred.rectangle((80, 50, 130, 100), fill = 0)
    # drawred.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Blackimage), epd.getbuffer(Redimage))

except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()

