from io import BytesIO
from PIL import Image
import sys

def data_to_img(data):
    fp = BytesIO(data)
    return Image.open(fp)

def img_to_data(img, fmt=None):
    fp = BytesIO()
    if not fmt:
        fmt = img.format
    img.save(fp, fmt) 
    return fp.getvalue()

def convert_image(data, fmt=None):
    img = data_to_img(data)
    return img_to_data(img, fmt)

def get_file_data(name):
    img = Image.open(name)
    print('img', img, img.format)
    return img_to_data(img)

if __name__ == "__main__":
    for name in sys.argv[1:]:
        data = get_file_data(name)
        print('in', len(data), data[:10])
        for fmt in ('gif', 'png', 'jpeg'):
            out_data = convert_image(data, fmt)