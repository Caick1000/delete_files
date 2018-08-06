from os import listdir, unlink, path
from os.path import getctime
from time import time

dir_path = 'var/log/'
dir_path_extension = ['asterisk', 'contact']
removable_file_extensions = ['.log']

current_time = time()

for f in os.listdir(dir_path):
    creation_time = os.path.getctime(f)
    if (current_time - creation_time) // (24 * 3600) >= 7:
        os.unlink(f)
        print('{} removed from directory {}'.format(f, dir_path))

for i in dir_path_extension:
    index_value = i
    full_path = dir_path + index_value[i]



def delete_files(dir_path):
    for file in listdir(dir_path):
        file_date = getctime(file)

        if (current_time - file_date) // (24 * 3600) >= 365 and removable_file_extensions in file[:-3]:
            print(file)
            # os.unlink(file)
        print('"{}" removed from directory "{}"'.format(file, dir_path))
