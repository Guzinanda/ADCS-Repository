'''
@ TITLE:    read_files.py
@ DATE:     25-03-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Exercise 14
'''

import sys


def read_text_file(filename):
    '''
    Reads a file and returns a list of int values.

    Parameters:
        read_text_file(filename): The file .txt name as a string.

    Returns:
        my_numbers: A list of int values. 
    '''
    
    try:
        file = open(filename, "r")

    except IOError:
        print(f"ERROR: The file {filename} does not exist...")
        sys.exit()  # raise

    else:
        my_values = []
        my_numbers = []

        for line in file:
            clean_line = line.rstrip()
            cleaned_line = clean_line.split(",")
            my_values.append(cleaned_line)

        for each_list in my_values:
            for each_value in each_list:
                my_numbers.append(int(each_value))

    return my_numbers


if __name__ == "__main__":
    print(f'Lists of numbers: {read_text_file("values1.txt")}')
    print(f'Lists of numbers: {read_text_file("values2.txt")}')
