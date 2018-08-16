import os

def add_to_path():
    user=os.getlogin()
    location = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(user)
    filename = 'desktop_wallpaper_changer.bat'
    file = os.path.join(location, filename)
    with open(file, 'w') as f:
        f.write(r'pythonw.exe C:\Users\Zico\AppData\Local\Programs\Python\Python36\Lib\site-packages\DesktopWallpaperChanger.py')
        f.close()

add_to_path()