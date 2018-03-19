from PIL import Image, ImageFile
import pytesseract

ImageFile.LOAD_TRUNCATED_IMAGES = True
code = ['7025', 'hxnk', 'mkck', 'gmd8', 'nmj3',
        'pzbw', 'cfau', 'zxrx', 'ty8g', 'fjmj']
for i in range(0, 10):
    path = "showImg/" + str(i) + '.jpg'
    image = Image.open(path)
    print(pytesseract.image_to_string(image) + ":" + code[i])
