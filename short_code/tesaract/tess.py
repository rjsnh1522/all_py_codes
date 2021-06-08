from PIL import image
import pytesseract


stss = pytesseract.image_to_string(Image.open('img.png'), lang='eng')

print(stss)