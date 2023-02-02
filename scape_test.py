import gdrive_tools
import numpy
from PIL import Image
from time import sleep
from datetime import datetime



def generateImage():
    a = numpy.random.rand(30,30,3) * 255
    im_out = Image.fromarray(a.astype('uint8')).convert('RGB')
    return im_out


def main():
    ''' Shows basic usage of the PiCamera functionality
        save a picture, then save a picture every 5 seconds over 30 seconds,
        change camera settings
    '''
    #Take five pictures in a row every 5 seconds
    folder = "ScapePhotos"
    print("Generating image Files...")
    for i in range(5):
        now = datetime.now()
        dtStr = now.strftime("%Y-%m-%d_%H.%M.%S.jpg")
        image = generateImage()
        image.save(dtStr)
        folder = "ScapePhotos"
        print("uploading: {}".format(dtStr))
        gdrive_tools.upload_file(folder, dtStr)
        sleep(5)


if __name__ == '__main__':
    main()
