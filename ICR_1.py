from PIL import Image
import pytesseract
import os

def get_captcha():
    
    im = Image.open('screenshot.png')
    
    #im_crop = im.crop((900, 1025, 1200, 1125)) 
    #headless
    #im_crop = im.crop((750, 1025, 1000, 1125)) 
    im_crop = im.crop((364, 502, 503, 532))

    im_crop.save('captcha.png', quality=95)

    captcha = pytesseract.image_to_string(Image.open('captcha.png'),config='--psm 8 -c tessedit_char_whitelist=0123456789')
    captcha = captcha.replace(" ", "").strip()

    path = os.getcwd()
    
    os.remove(path+"/captcha.png")
    os.remove(path+"/screenshot.png")

    return captcha
    
