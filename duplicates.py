import os
import sys
from os.path import getsize
from collections import defaultdict


def get_all_files(path):
    dict_of_files = {}
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            file_info = (filename, getsize(full_path))
            dict_of_files.setdefault(file_info, []).append(full_path)
    return dict_of_files


def print_duplicates(dict_of_files):
    for file_info, full_path in dict_of_files.items():
        if len(full_path) > 1:
            print('file - {}\nfile paths - {}\n'.format(file_info, full_path))


if __name__ == '__main__':
    path = sys.argv[1]

    if not os.path.isdir(path):
        exit('The directory {} does not exist!'.format(path))
    else:
        print_duplicates(get_all_files(path))
