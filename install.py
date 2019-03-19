#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Will Assad"
__copyright__ = "Copyright 2018, Convert"
__credits__ = ["Will Assad", "Devansh Kaloti"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "DKSources"
__email__ = "willassadcode@gmail.com"
__status__ = "Production"

import os, platform, sys, ctypes

# Check if file is being run by admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class InstallConvert():



    def __init__(self):
        print('+------------------------------------------------------+')
        print('|             Installing IntelliJ Converter            |')
        print('|                 Developed By DkSources               |')
        print('|                  Edited by Will Assad                |')
        print('+------------------------------------------------------+')
        self.homedir = os.path.expanduser('~')



    def setup(self):
        if platform.system() == "Darwin":
            self.mac_osx_install_route()
        if platform.system() == "Windows":
            if not is_admin():
                print("Please run install.py with admin privileges")
                print("You can run it as 'runas /user:{ADMINUSER} py install.py'")
                sys.exit()
            else:
                self.windows_install_route()

        with open(os.path.join(os.path.expanduser('~'), "path.txt"),"w") as f:
            f.write(os.getcwd())

    def mac_osx_install_route(self):
        # spdir = os.path.join(self.homedir, "DKsources", "convert")
        # os.system("chmod +x ./convert.py")
        # os.system("mkdir " + spdir)
        # os.system('export PATH="$PATH:$HOME/bin"')
        # os.system("cp -r "+ self.homedir + spdir)

        os.system("chmod +x ./convert.py")
        os.system('export PATH="$PATH:$HOME/bin"')
        os.system("ln -s " + os.getcwd() + "/convert.py /usr/local/bin/convert")

    def windows_install_route(self):
        os.system("mkdir " + os.path.join(self.homedir, "DKsources", "convert"))
        os.system("xcopy \"" + os.getcwd() + "\" \"" + os.path.join(self.homedir, "DKsources", "convert") + "\" /s /y")
        os.system("SET PATH \"%PATH%;" + os.path.join(self.homedir, "DKsources", "convert") + "\\")
        os.system("SETX PATH \"%PATH%;" + os.path.join(self.homedir, "DKsources", "convert") + "\\")


if __name__ == "__main__":
    installer = InstallConvert()
    installer.setup()
    print("INSTALLED successfully.")
