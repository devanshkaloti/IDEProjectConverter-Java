# MIT License
# Devansh Kaloti devansh@dksources.com Contact for support
# Convert Intellij Projects to Netbeans

import shutil


def openFile(file, permission):
    try:
        return open(file, permission)
    except FileNotFoundError as e:
        print("** File Not Found %s**" %file)
    except PermissionError:
        print("** Insufficient permissions to open file %s**\n\n" %file)
    except Exception:
        print("** Unknown Error While Opening File:  %s**\n\n" %file)

# Reset the output folder to template.
def resetFolder():
    with openFile("template/project.xml", "r") as templateProjectXML:
        with openFile("nbproject/project.xml", "w") as outputProjectXML:
            outputProjectXML.write(templateProjectXML.read())

    with openFile("template/project.properties", "r") as templateProperties:
        with openFile("nbproject/project.properties", "w") as outputProperties:
            outputProperties.write(templateProperties.read())


# Coping contents of src folder to final folder
def copyFolder(src, dist):
    try:
        shutil.copytree(src, dist)  # Copy files
    except FileExistsError:
        print("Files Existed")
    except FileNotFoundError:
        print("Folder could not be located: " + dist)
    except Exception as e:
        print("Unknown Error")

# Get the project name, by finding last in pathname
def getProjectName(path):
    return str(path).split("/")[path.count("/")]


# Replace the Project Name In XML file
def replaceProjectName():
    global srcPath
    file = openFile("nbproject/project.xml", "r")
    lines = file.readlines()
    file.close()

    for i,line in enumerate(lines):
        if "<name>******************</name>" in line:
            lines[i] = "<name>%s</name>\n" %getProjectName(srcPath)


    with openFile("nbproject/project.xml", "w") as file:
        file.write(''.join(lines))


# MAIN CODE
print("This program will duplicate your project and make it NetBeans Compatible.")
print("Please make sure your programming files are located under 'src/'\n")

srcPath = input("Enter Source Path: ").strip(" ")
dstPath = srcPath + "NB"

replaceProjectName()
copyFolder(srcPath + "/src", dstPath + "/src")  # Copy coding
copyFolder("nbproject", dstPath + "/nbproject")  # Copy settings

resetFolder()
print("\n\nYour project has been converted!\nPlease look in your source directory.")