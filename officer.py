# My mom had a USB thumb drive that was overheating and about to fail.
# chkdsk barfed out a bunch of orpahned .chk files. I looked at them 
# from a laptop running linux and found a bunch of 'zip archives' 
# identified by the auto-thumbnail feature. I copied all of these 
# files off somewhere, renamed them to .ZIP, and then started peeking
# inside. It turns out that most of these zip archives were actually
# MS Office documents (mostly Word and Excel), so I wrote this script
# based on some examples and a little bit of duct tape to identify
# the kind of file we're most likely working with and rename it with
# the right file ext so that my mom can review the orphaned files.
#
# This is their story. 
#
# 2020-08-24 MaconiP with lots of help from the Googletron and 
# especially the Python standard library documentation. 

from os import listdir, rename
from os.path import isfile, join, dirname, split, basename, abspath
from zipfile import ZipFile, is_zipfile
import shutil

files = [f for f in listdir ('.') if isfile(join('.',f))]
for myfile in files:
    try:
        if (is_zipfile(myfile)):
            with ZipFile(myfile, mode='r') as zip:
                dirs = list(set([dirname(x) for x in zip.namelist()]))
                topdirs = [split(x)[0] for x in dirs]
                if 'word' in topdirs:
                    newfile = myfile.replace('.ZIP','.DOCX')
                    shutil.copyfile(abspath(myfile), newfile)
                    print(f"{myfile} copied to {newfile}")
                elif 'xl' in topdirs:
                    newfile = myfile.replace('.ZIP','.XLSX')
                    shutil.copyfile(myfile, newfile)
                    print(f"{myfile} copied to {newfile}")
        else:
            print (f"{myfile} is not a zip file.")
    except:
        print (f"Something is wrong with {myfile}")
