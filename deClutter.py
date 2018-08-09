import os, shutil

curuser = os.getlogin()

path = "C:/Users/" + curuser + "/Desktop/"
clutterpath = path + "Clutter/"
imagepath = path + "Images/"
pptpath = path + "Presentations/"
docpath = path + "Documents/"
mediapath = path + "Media/"

docexts = ['.txt', '.doc', '.docx', '.xlsx','.xlsm', '.pdf']
imageexts = ['.jpg', '.jpeg', '.png', '.gif', '.tif', '.tiff']
pptexts = ['.ppt', '.pptx', '.pptm']
mediaexts = ['.mp3', '.wav', '.mp4', '.mov']

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
    
if not os.path.exists(mediapath):
    ls.makedirs(mediapath)

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
    # Handle images here
    elif ext in imageexts:
        src = path + f
        dst = imagepath + f
        shutil.move(src,dst)
    # Handle ppts here
    elif ext in pptexts:
        src = path + f
        dst = pptpath + f
        shutil.move(src,dst)
    elif ext in mediaexts:
        src = path + f
        dst = mediapath + f
        shutil.move(src,dst)
    # Send everything else to the clutter folder
    else:
        src = path + f
        dst = clutterpath + f
        shutil.move(src,dst)
        
