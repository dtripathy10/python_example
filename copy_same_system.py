'''
This script will copy your entire file/folder structure to the server.
And, it will skip file/folder such as git,nbproject etc.
'''
# Import the os module, for the os.walk function
import os
import sys
# This module helps for high level operation on file or folder.
# Specifically on file/folder modification or deletion
import shutil;

# import ftp library

import ftplib

import stat#needed for file stat

def remShut(*args):
    func, path, _ = args #onerror returns a tuple containing function, path and     exception info
    os.chmod(path, stat.S_IWRITE)
    os.remove(path)

# Set the directory you want to start from
sourceDir = 'H:/wamp/www/virtual_lab'
# Set the directory you want to copy(The directory should not exist)
destinationDir='tmp'
#ignore patterns
IGNORE_PATTERNS = ('*.pyc','CVS','.git','tmp','.svn','nbproject','*.ini')

# check, if destination directory is present or not
if os.path.exists(destinationDir):
    shutil.rmtree(destinationDir,onerror = remShut) 
    print("The tmp directory is deleted");
    
#copy the directory
print("folder copy is startd.......")
shutil.copytree(sourceDir, destinationDir,True,ignore=shutil.ignore_patterns(*IGNORE_PATTERNS))
print("Finished the copying job........")

#recursively go to the destination directory


for dirName, subdirList, fileList in os.walk(destinationDir):
    print('Found directory: %s' % os.path.abspath(dirName))
    for fname in fileList:
        print('\t%s' % os.path.abspath(fname))



# connect to ftp

ftp = ftplib.FTP("bighome.iitb.ac.in")
ftp.login("gpatil", "belgaum!")
print(ftp.getwelcome())


#close the connection
ftp.quit()
ftp.close()


# End of the exeution
print("------------------------------------------")
print("Execution completed....")
print("------------------------------------------")
os.system("pause")




