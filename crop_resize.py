from PIL import Image
import os, sys

path = "./raw_images/"
saved_location = "./edited_images/"
dirs = os.listdir( path )
coords = (0, 500, 3000, 3500) ## imagen original 3120x4160

def crop():
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    for item in dirs:
        if os.path.isfile(path+item):
            image_obj = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            # print(e) extension
            # print(f) path
            # cropped_image = image_obj.crop(coords)
            # cropped_image.save(f + '.JPEG')
			# cropped_image.show()
            im = image_obj.crop(coords)
            imResize = im.resize((300,300), Image.ANTIALIAS)
            imResize.save(f + '_sq.jpg', 'JPEG', quality=90)

"""			
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((300,300), Image.ANTIALIAS)
            imResize.save(f + '_resized.jpg', 'JPEG', quality=90)
"""

crop()
#resize()