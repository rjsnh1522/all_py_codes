

import os, time
# import ipdb
import zipfile

def get_file():
    top = os.getcwd()
    path = "/Users/logan/Downloads"
    # for (dirname, dirs, files) in os.walk(path):        
            # for filename in files:
    filename = 'git_zip.zip'
    filepath = (path +"/"+filename)
        # is_locked(filepath)
    unzip_file(filepath)



def unzip_file(filepath):
    # print(filepath.infolist())
    zip_ref = zipfile.ZipFile(filepath, 'r')
    for zinfo in zip_ref.infolist():
       isenc = zinfo.flag_bits & 0x1
       if isenc:
            print("r")
    # zip_ref.extractall("/Users/logan/Downloads/uncomp")
    # zip_ref.close()

def is_locked(filepath):
    """Checks if a file is locked by opening it in append mode.
    If no exception thrown, then the file is not locked.
    """
    locked = None
    file_object = None
    if os.path.exists(filepath):
        try:
            # print("Trying to open %s." % filepath)
            buffer_size = 8
            # ipdb.set_trace()
            # Opening file in append mode and read the first 8 characters.
            file_object = open(filepath, 'a', buffer_size)
            if file_object:
                # print("%s is not locked." %filepath)
                locked = False
        except IOError as message:
            print("File is locked (unable to open in append mode). %s." %message)
            locked = True
        finally:
            if file_object:
                file_object.close()
                # print("%s closed." %filepath)
    else:
        # print("%s not found." %filepath)
        pass
    return locked



get_file()