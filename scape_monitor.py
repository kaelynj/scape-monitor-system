import gdrive_tools
from picamera import PiCamera
from datetime import datetime

def capture(fileName):
    camera = PiCamera()
    camera.capture(fileName)
    print("Captured Image w/ Name: {}".format(fileName))
    return None

def main():
    ''' Shows basic usage of the PiCamera functionality
        save a picture, then save a picture every 5 seconds over 30 seconds,
        change camera settings
    '''
    folder = "ScapePhotos"
    now = datetime.now()
    dtStr = now.strftime("%Y-%m-%d_%H.%M.%S.jpg")
    capture(dtStr)
    print("uploading: {}".format(dtStr))
    gdrive_tools.upload_file(folder, dtStr)




if __name__ == '__main__':
    main()
