import os, shutil

curuser = os.getlogin()

path = "C:/Users/" + curuser + "/Desktop/"
clutterpath = path + "Clutter/"
imagepath = path + "Images/"
pptpath = path + "Presentations/"
docpath = path + "Documents/"

docexts = ['.txt', '.doc', '.docx', '.xlsx','.xlsm', '.pdf']
imageexts = ['.jpg', '.jpeg', '.png', '.gif', '.tif', '.tiff']
pptexts = ['.ppt', '.pptx', '.pptm']

files = os.listdir(path)

# Check if organizational folders already exist
if not os.path.exists(clutterpath):
    os.makedirs(clutterpath)
    
if not os.path.exists(imagepath):
    os.makedirs(imagepath)
    
if not os.path.exists(pptpath):
    os.makedirs(pptpath)
    
if not os.path.exists(docpath):
    os.makedirs(docpath)

for f in files:
    # Split the file extension from the file name
    name, ext = os.path.splitext(f)
    
    # Ignore the desktop .ini file and any shortcuts
    if ext == '.ini' or ext == '.lnk':
        pass
    # Ignore any pre-existing folders
    elif ext == '':
        pass
    # Handle documents here
    elif ext in docexts:
        src = path + f
        dst = docpath + f
        shutil.move(src,dst)
        #print (f + ' belongs in the Document folder.')
    # Handle images here
    elif ext in imageexts:
        src = path + f
        dst = imagepath + f
        shutil.move(src,dst)
        #print (f + ' belongs in the Image folder.')
    # Handle ppts here
    elif ext in pptexts:
        src = path + f
        dst = pptpath + f
        shutil.move(src,dst)
        #print (f + ' belongs in the PowerPoint folder.')
    # Send anything else to the clutter folder
    else:
        src = path + f
        dst = clutterpath + f
        shutil.move(src,dst)
        #print ("I'm not sure what " + f
               #+ " is so I'm putting it in the clutter folder.")
        
