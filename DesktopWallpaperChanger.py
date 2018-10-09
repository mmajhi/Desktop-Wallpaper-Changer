import ctypes
import os
import time
from pynput.keyboard import Key,Controller
import Bing


def closeTerminal():
    keyboard=Controller()
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)

def changeWallpaper(image_path):
    start=time.time()
    end=time.time()
    while True:
        for dirname,dirnames,filenames in os.walk(image_path):
            for file_name in filenames:
                if (end-start)//3600 > 6:
                    try:
                        Bing.wallpaper_of_the_day(image_path)
                        start=time.time()
                    except:
                        pass
                if file_name.endswith('.png') or file_name.endswith('.jpg'):
                    image=os.path.join(image_path,dirname,file_name)
                    SPI_SETDESKTOPWALLPAPER=20
                    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER,0,image,3)
                    time.sleep(30)
                end=time.time()

def main():
    closeTerminal()
    #configure own folder
    image_path = r'D:\Wallpapers'
    try:
        os.makedirs(image_path)
    except:
        pass
    try:
        Bing.wallpaper_of_the_day(image_path)
    except:
        pass
    changeWallpaper(image_path)

if __name__=='__main__':
    main()
