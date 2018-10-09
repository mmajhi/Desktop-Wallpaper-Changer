# Desktop Wallpaper Changer
 
**(Windows Only)**

Automatically changes the Desktop Background from a given directory.

It also downloads the Bing Wallpaper of the day and adds it to the directory each day.

### Synopsis
Python Script for automatically downloading and changing the desktop wallpaper to Bing Photo of the day and giving a slideshow from a given directory. The script runs automatically at the startup and works on Windows only.

### How does it gets the image?
It grabs images exactly the same way Microsoft uses to put it up on its page - using XML/RSS/JSON. You can't scrape the website directly. After searching on the internet for long I found out the link - http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-US

Here we can get data in any of the formats but substituting the value of format=[value] in the link.

idx denotes the day before the current day. idx=0 means current day, idx=1 means yesterday and so on. n is an integer denoting the number of days before the day denoted by idx. It grabs data about all the n number of images. mkt denotes the area. The list of areas can be found from https://msdn.microsoft.com/en-us/library/dd251064.aspx .The default mkt is 'en-US', but you can change it as required.

### Installer
Executable file uploaded

**Bing.exe** file adds itself to the windows startup and runs in the background forever. It checks for new bing daily wallpaper and gives a slideshow of the images present in the directory 'F:/Wallpapers'. If the directory not present it is created automatically.
**Bing_daily.exe** file checks for new bing daily wallpaper when executed.**No requirements.**

Fully automated Desktop-Wallpaper-Changer installation and configuration!Edit the image_path in main() in DesktopWallpaperChanger.py to your desired directory. No need to add the script to your Startup list or copy paste it or etc.. The Installer does everything for you!

You just need to run the **_setup.bat_** file once after the downloading the whole package.

The process will continue even after restarting the system.

#### Requirement
python 3.5>=

### Author
**Mayukh Majhi** and [contributors](https://github.com/mmajhi/Desktop-Wallpaper-Changer/network/members)
