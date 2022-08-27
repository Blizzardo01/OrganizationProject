import os 
import shutil
import datetime


path = "C:/Users/jacob/Desktop/Test"
files = os.listdir(path)
listValidFiles = []
imgExts = [".png", ".jpg", ".jpeg", ".gif",".svg"]
currentDate = datetime.date.today().__str__()

def is_image(file):
    return os.path.splitext(file)[1] in imgExts

#start of main    
    #video folders next, etc etc

for file in files:
    rootext = os.path.splitext(p= os.fspath(files[0]))

    if rootext[1] is not None:
        listValidFiles.append(file.__str__);

if len(listValidFiles) > 0:

    if (os.path.exists(f'{path}/{currentDate}')):
        print('Error: date path already created')

    else:
        os.mkdir(path + "/" + currentDate)

if (os.path.exists(f'{path}/{currentDate}/Images/')):
    print('Error: Image path already created')

else:
    os.mkdir(f'{path}/{currentDate}/Images/')
    #add more types of files here
for file in listValidFiles:
    if is_image(file):
        shutil.move(file, f'{path}/{currentDate}/Images/')
