'''
@ TITLE:    ValueSorter.py
@ DATE:     20-04-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Logging
'''

# 00_ Import logging library
import logging

# 01_ Create and configure logger (file)
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logtest.log", 
level = logging.DEBUG, 
format = LOG_FORMAT, 
filemode = 'w')

logger = logging.getLogger()
print(logger.level)

'''
logger.debug("This is a harmless debug message.")
logger.info("This is just some useful info.")
logger.warning("I'm sorry, but you can't do that.")
logger.error("Did you try to divide by zero?")
logger.critical("The entire internet is on fire!")
'''


class ValuesSorter:
    array = []
    sorted_array = []

    # Phase 1
    def set_input_data(self, file_path_name):

        try:
            logger.debug(f"01 The program will try to read the file {file_path_name}...")
            file = open(file_path_name, "r")

        except IOError:
            logger.error(f"02 Oh no! The file {file_path_name} wasen't found...")
            #print(f"ERROR: The file {file_path_name} does not exist...")

        else:
            logger.info(f"02 The file {file_path_name} was read successfully!...")

            logger.debug("03 The program will try to create an array of int data...")
            for line in file:
                clean_line = line.rstrip()
                cleaned_line = clean_line.split(",")
                for each_value in cleaned_line:
                        try:
                            self.array.append(int(each_value))
                        except ValueError:
                            compatible_file = False
                        else:
                            compatible_file = True
                            continue
            
            if compatible_file == True:
                logger.info(f"04 The data in {file_path_name} was compatible!...")
                #print(f"OK!: The values are: {self.array}")
            else:
                logger.error(f"04 Oh no! The data in {file_path_name} wasn't compatible...")
                #print(f"ERROR: The file {file_path_name} has not compatible data...")


    # Phase 2
    def execute_merge_sort(self, arr):
       
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return self.execute_merge_sort(less) + [pivot] + self.execute_merge_sort(greater)


    # Phase 3
    def set_output_data(self, file_path_name):
        
        try:
            logger.debug("05 The program will try to create a file with sorted data...")
            new_file = open(file_path_name, "w+")

        except IOError:
            logger.error(f"06 The program wasn't able to write the file...")
            #print(f"ERROR: The file {file_path_name} was not created...")

        else:
            for data in self.sorted_array:
                new_file.write(str(data) + ",")
            logger.info(f"06 The program was able to write the file!...")

            #print(f"OK!: The file {file_path_name} was created!...")


def main():
    print("")
    print("CASE 1 /////////////////////")
    sort1 = ValuesSorter()
    sort1.set_input_data("values1.txt")
    sort1.sorted_array = sort1.execute_merge_sort(sort1.array)
    sort1.set_output_data("values3.txt")

    #print("")
    #print("CASE 2 /////////////////////")
    #sort2 = ValuesSorter()
    #sort2.set_input_data("values2.txt")

    #print("")
    #print("CASE 3 /////////////////////")
    #sort3 = ValuesSorter()
    #sort3.set_input_data("values4.txt")


if __name__ == "__main__":
    main()
