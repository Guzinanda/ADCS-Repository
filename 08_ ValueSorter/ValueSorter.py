'''
@ TITLE:    ValueSorter.py
@ DATE:     25-03-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Exercise 20
'''

class ValuesSorter:

    array = []
    sorted_array = []

    # Phase 1: Reads the values from the CSV, saves them into an sortable array and checks if all elements are the same type_________________ (OK!)
    def set_input_data(self, file_path_name):
        '''Reads the values from the CSV, saves them into an sortable array and checks if all elements are the same type.
        
        Paramenters:
            file_path_name(str): Name of the document to read.
        
        Returns:
            n/a
        '''
        try:
            file = open(file_path_name, "r")

        except IOError:
            print(f"ERROR: The file {file_path_name} does not exist...")

        else:
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
                print(f"OK!: The values are: {self.array}")
            else:
                print(f"ERROR: The file {file_path_name} has not compatible data...")


    # Phase 2: Sorts the values in array with the Quick Sort Algorithm_____________________________ (OK!)
    def execute_merge_sort(self, arr):
        '''Sorts the values in array with the Quick Sort Algorithm
        
        Paramenters:
            arr(array): Takes an array 
        
        Returns:
            arr(array): It returns the same arrray sorted.
        '''
       
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return self.execute_merge_sort(less) + [pivot] + self.execute_merge_sort(greater)


    # Phase 3: Creates the file where the sorted array will be saved_______________________________ (OK!)
    def set_output_data(self, file_path_name):
        '''Creates the file where the sorted array will be saved
        
        Paramenters:
            file_path_name(str): The name of the file.
        
        Returns:
            n/a
        '''
        
        try:
            new_file = open(file_path_name, "w+")

        except IOError:
            print(f"ERROR: The file {file_path_name} was not created...")

        else:
            for data in self.sorted_array:
                new_file.write(str(data) + ",")
            print(f"OK!: The file {file_path_name} was created!...")


def main():

    print("")
    print("CASE 1 /////////////////////")
    sort1 = ValuesSorter()
    sort1.set_input_data("values1.txt")
    sort1.sorted_array = sort1.execute_merge_sort(sort1.array)
    sort1.set_output_data("values3.txt")

    print("")
    print("CASE 2 /////////////////////")
    sort2 = ValuesSorter()
    sort2.set_input_data("values2.txt")

    print("")
    print("CASE 3 /////////////////////")
    sort3 = ValuesSorter()
    sort3.set_input_data("values4.txt")


if __name__ == "__main__":
    main()