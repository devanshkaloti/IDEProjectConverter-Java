#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Devansh Kaloti"
__copyright__ = "Copyright 2018, Convert"
__credits__ = ["Devansh Kaloti", "Will Assad"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "DKSources"
__email__ = "devansh@dksources.com"
__status__ = "Production"

"""main.py will convert Intellij Projects
   to be Netbeans compatible.
"""
import shutil, sys, os

homedir = os.path.expanduser('~')
pathToPath = os.path.join(homedir, "path.txt")

try: #attempt to read the users path from path.txt
    with open(pathToPath,"r") as f:
        customPath = f.read()
except FileNotFoundError: #if the user has run install
    print("ERROR: Must run install.py")
    quit()

#get the correct file path depending on where this file is located
def filepath(folder, filename):
    return customPath + "/" + folder + "/" + filename

#returns an instance of a file if no errors occur
def openFile(file, permission):
    try:
        return open(file, permission)
    except FileNotFoundError as e:
        print("** File Not Found %s**" %file)
    except PermissionError:
        print("** Insufficient permissions to open file %s**\n\n" %file)
    except Exception:
        print("** Unknown Error While Opening File:  %s**\n\n" %file)

    quit()

# Reset the output folder to template.
def resetFolder():
    with openFile(filepath("template","project.xml"), "r") as templateProjectXML:
        with openFile(filepath("nbproject","project.xml"), "w") as outputProjectXML:
            outputProjectXML.write(templateProjectXML.read())

    with openFile(filepath("template","project.properties"), "r") as templateProperties:
        with openFile(filepath("nbproject","project.properties"), "w") as outputProperties:
            outputProperties.write(templateProperties.read())


# Coping contents of src folder to final folder
def copyFolder(src, dist):
    print(src, dist)
    try:
        shutil.copytree(src, dist)  # Copy files
    except Exception as e:
        print(e)

# Get the project name, by finding last in pathname
def getProjectName(path):
    return str(path).split("/")[path.count("/")]


# Replace the Project Name In XML file
def replaceProjectName(srcPath):
    #global srcPath
    file = openFile(filepath("nbproject","project.xml"), "r")
    lines = file.readlines()
    file.close()

    for i,line in enumerate(lines):
        if "<name>******************</name>" in line:
            lines[i] = "<name>%s</name>\n" %getProjectName(srcPath)


    with openFile(filepath("nbproject","project.xml"), "w") as file:
        file.write(''.join(lines))


#main logic, convert project to NetBeans
def main():
    try: file_name = sys.argv[1]
    except IndexError:
        print("ERROR: Expected 1 Argument Containing File Path to convert ex. 'convert ...'")
        return

    srcPath = file_name.strip(" ")
    dstPath = srcPath + "NB"

    replaceProjectName(srcPath)
    copyFolder(srcPath + "/src", dstPath + "/src")  # Copy coding
    copyFolder(filepath("nbproject",""), dstPath + "/nbproject")  # Copy settings

    resetFolder()
    print("\n\nYour project has been converted!\nPlease look in your source directory.")


if __name__ == '__main__':
    main()
