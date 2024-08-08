from PIL import Image
from PIL import ImageFilter

filename = "tt.jpg"

with Image.open(filename) as img:
    img.load()
img.show()

img = img.filter(ImageFilter.CONTOUR)
img.show()
