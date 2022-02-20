import random
from PIL import Image
import string

class Img():
    def image_resize(img,size):
        im = Image.open(img)
        new_w = int(size)
        new_h = int((new_w/3)*4)
        image_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        new_size = im.resize((new_w,new_h))
        img_n = image_name+'.jpg'
        new_size.save(img_n)
        print("Image Saved to Python file location")

    def image_ext(img,ext):
        im = Image.open(img)
        image_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        img_ex =image_name+"."+ext
        im.save(img_ex)

