from os import listdir, unlink, path, walk
from os.path import getctime, isfile
from time import time


dir_path = 'D:/talkeen/test/var/log/'
dir_path_extension = ['asterisk/', 'contact/']
removable_file_extensions = ['log']

current_time = time()
minimum_date = 365

for i in dir_path_extension:
    index_value = i
    full_path = dir_path + index_value



def delete_files(path):

    for root, dirs, files in walk(path):
        for file in files:
            print(file, files, root)
            file_date = getctime(file)
            # if (current_time - file_date) // (24 * 3600) >= minimum_date and removable_file_extensions in file[-3:] and isfile(path):
            if isfile(path + file):
                # unlink(path + file)
                print('"{}" removed from directory "{}"'.format(file, path))


delete_files(dir_path)