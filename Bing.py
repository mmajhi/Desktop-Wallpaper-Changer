import urllib3
import os
import re
import urllib.request
import ctypes
from bs4 import BeautifulSoup
import winsound
import time

urllib3.disable_warnings()


# Fucntion For Extracting Image Url and Image Details From xml
def get_image_url(xml):
    # Url and name Pattern
    pattern='<url>(.*?)</url>'
    http = urllib3.PoolManager()
    raw_xml = http.request('GET', xml)
    soup = BeautifulSoup(raw_xml.data, features='html5lib')
    img_url=re.search(pattern,str(soup)).group(1)
    # Complete Url
    bing = 'https://www.bing.com' + img_url
    return bing

# Function for Downloading Image
def download_image(url,img_path):
     folder=os.path.join(img_path,'Bing')
     try:
         os.makedirs(folder)
     except:
         pass
     img_name = url.split('/')[-1]
     filename = os.path.join(folder, img_name)
     if os.path.exists(filename):
         return

     urllib.request.urlretrieve(url,filename)
     #Set the new image as the current wallpaper
     changewallpaper(filename)

def changewallpaper(image):
    SPI_SETDESKTOPWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, image, 3)
    # Notify the user about new wallpaper
    winsound.Beep(5000,200)
    time.sleep(30)


def wallpaper_of_the_day(img_path):
    '''country = ['ar-XA', 'bg-BG', 'cs-CZ', 'da-DK', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en-AU', 'en-CA',
               'en-GB', 'en-ID', 'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-PH', 'en-SG', 'en-US', 'en-XA',
               'en-ZA', 'es-AR', 'es-CL', 'es-ES', 'es-MX', 'es-US', 'es-XL', 'et-EE', 'fi-FI', 'fr-BE',
               'fr-CA', 'fr-CH', 'fr-FR', 'he-IL', 'hr-HR', 'hu-HU', 'it-IT', 'ja-JP', 'ko-KR', 'lt-LT',
               'lv-LV', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sk-SK',
               'sl-SL', 'sv-SE', 'th-TH', 'tr-TR', 'uk-UA', 'zh-CN', 'zh-HK', 'zh-TW']'''
    xml_file = 'https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=2&mkt=en-US'
    img_url = get_image_url(xml_file)
    download_image(img_url,img_path)

