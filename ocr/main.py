import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
img = cv2.imread('new2.png')

# OCR using pytesseract
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

print("Extracted Text:")
print(text)

