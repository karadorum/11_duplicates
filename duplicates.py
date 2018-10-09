import os
import sys
from os.path import getsize
import pprint


def get_all_files(path):
    dict_of_files = {}
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            file_info = (filename + ' - ' + str(getsize(full_path)))
            dict_of_files.update({full_path: file_info})
    return dict_of_files


def check_for_duplicates(dict_of_files):
    flipped = {}
    list_of_duplicates = {}
    for key, value in dict_of_files.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)

    for key, value in flipped.items():
        if len(value) > 1:
            list_of_duplicates.update({key: value})
    return list_of_duplicates


if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except FileNotFoundError:
        exit('file not found')
    except IndexError:
        exit('file argument is empty')

    result = check_for_duplicates(get_all_files(path))
    pprint.pprint(result, width=1)
