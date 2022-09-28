import time
import subprocess
import cv2

def image_position(small_image, big_image):
    img_rgb = cv2.imread(big_image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(small_image, 0)
    height, width = template.shape[::]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF)
    _, _, top_left, _ = cv2.minMaxLoc(res)
    bottom_right = (top_left[0] + width, top_left[1] + height)
    return (top_left[0]+bottom_right[0])//2, (top_left[1]+bottom_right[1])//2

def click(tap_x, tap_y):
    adb("adb shell input tap {} {}".format(tap_x, tap_y))

def adb(command):
    subprocess.call(command,shell=True)
    #proc = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, shell=True)
    #(out, _) = proc.communicate()
    #return out.decode('utf-8')

path_of_image_of_whatsapp_button='/Users/kama/Documents/work/documents/whatsapp_loeschen.png'

while True:
    print(f'Start')
    #subprocess.call("adb shell input tap 1300 220",shell=True)

    adb(f'adb shell input tap 1300 220')
    time.sleep(300/1000)

    # take screenshot of page
    adb(f"adb exec-out screencap -p > screenshot.png")
    # get the position of the whatsapp send button using template matching
    x,y = image_position(path_of_image_of_whatsapp_button, '/Users/kama/Documents/work/documents/screenshot.png')
    # click the button with the help of x and y
    click(x,y)
    time.sleep(300/1000)

    adb(f'adb shell input tap 1020 1850')

    time.sleep(300/1000)

    print(f'Successfully deleted picture')
