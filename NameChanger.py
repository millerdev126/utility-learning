import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory
import win32gui
import re

def ChangeNames():

    # Get a target folder from the user
    read = input("Using this tool will rename all files in target folder." + '\n' + \
                 "Be very careful when selecting your folder. Continue? (Y/N) ")
    if read == 'Y' or read == 'y': 
        # Hide root window from Tkinter
        Tk().withdraw()

        # Open a dialog to let user navigate to the desired folder
        path = askdirectory()

        cmd = win32gui.FindWindow(None, 'C:\windows\py.exe')
        win32gui.SetForegroundWindow(cmd)
        
        # Find out if user wants to add a date to the new name, and get that too, if so
        datebool = input("Do you want to include a date? (Y/N) ")
        if datebool == 'Y' or datebool == 'y':
            date = input('\n' + "What date should be included? " + '\n' +
                         "ie: 10-23-18, 2008, Dec 06, 1980" +'\n' +
                         'Just avoid the following characters: \/:*?"<>|' + '\n')

        # Get a base name from the user, something descriptive like 'Dad's Birthday'
        basename = input("What would you like me to name these files? " + '\n')

        # Generate a list of files in the target folder, and start a counter
        files = os.listdir(path)
        filecount = 1

        # For every file in the folder...
        for file in files:

            # Keep track of file extensions so we don't lose functionality
            name, ext = os.path.splitext(file)

            # ...assemble the new name based on the various pieces given by the user
            if datebool == 'Y' or datebool == 'y':
                newname = str(filecount) + ' ' + basename + ' ' + date + ext
            else:
                newname = str(filecount) + ' ' + basename + ext

            # Apply the new name and increment the file count
            os.replace(path + "\\" + file, path + "\\" + newname)
            filecount = 1 + filecount

        print ('Your Files are Ready!')
    else:
        exit()

ChangeNames()
