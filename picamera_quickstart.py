from picamera import PiCamera
from time import sleep


def main():
    ''' Shows basic usage of the PiCamera functionality
        save a picture, then save a picture every 5 seconds over 30 seconds,
        change camera settings
    '''
    camera = PiCamera()

    camera.capture('/home/pi/Desktop/image.jpg')

    #Take five pictures in a row every 5 seconds
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)

    #Change settings around
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.capture('/home/pi/Desktop/max.jpg')


if __name__ == '__main__':
    main()
