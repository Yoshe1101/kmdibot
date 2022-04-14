from PIL import Image
import cv2
from pytesseract import image_to_string
import os
def get_captcha():
    try:
        im = Image.open('screenshot.png')
    except: 
        print("no screenshot has been taken")
    #with heead
    im_crop = im.crop((900, 1025, 1200, 1125)) 

    #headless
    #im_crop = im.crop((750, 1025, 1000, 1125)) 

    im_crop.save('captcha.png', quality=95)

    img = cv2.imread("captcha.png")
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w*2, h*2))
    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
    thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    txt = image_to_string(thr)
    path = os.getcwd()
    
    #os.remove(path+"/captcha.png")
    #os.remove(path+"/screenshot.png")
    txt_filtered = ''
    for i in txt:
        if i in '0123456789':
            txt_filtered += i

    return txt_filtered
