from os import listdir, unlink, path
from os.path import getctime, isfile
from time import time


dir_path = 'var/log/'
dir_path_extension = ['asterisk', 'contact']
removable_file_extensions = ['log']

current_time = time()
minimum_date = 365

for i in dir_path_extension:
    index_value = i
    full_path = dir_path + index_value



def delete_files(dir_path):

    for file in listdir(dir_path):
        file_date = getctime(dir_path + file)
        # if (current_time - file_date) // (24 * 3600) >= minimum_date and removable_file_extensions in file[-3:] and isfile(dir_path):
        if isfile(dir_path):
            print(file, file[:-3])
            # os.unlink(file)
            print('"{}" removed from directory "{}"'.format(file, dir_path))

    
delete_files('D:/talkeen/test/')