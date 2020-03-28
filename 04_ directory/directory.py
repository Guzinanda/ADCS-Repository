'''
@ TITLE:    directory.py
@ DATE:     25-03-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Exercise 15
'''

def menu():
    '''
    Prints in console the menu.
    '''
    print(""" 
    WHAT DO YOU WANT TO DO...?
    ____________________________ 
    [1]  Create a new record *
    [2]  Combine records in a file *
    [3]  Check records from a file *
    [4]  Search and get data from a given record *
    [5]  Exit *
    """)
    option_selected = int(input("Option_ "))
    return option_selected


def create_record():
    record_name = input("Where do you want to save it?_ ")
    
    answer = "y"
    while answer != "n":
        add_record = open(record_name, 'a')
        new_name = input("- Whats the name?_ ")
        new_address = input("- Whats the address?_ ")
        new_phone = input("- Whats the phone?_ ")
        new_email = input("- Whats the email?_ ")
        add_record.write("\n" + new_name + ",")
        add_record.write(new_address + ",")
        add_record.write(new_phone + ",")
        add_record.write(new_email)
        print("Done!...\n")
        answer = input("Do you want to add another record [y/n]?_")


def combine_records():
    combined_document_name = input("Named the combined document_ ")
    combined_document = open(combined_document_name, "a")
    print("Which records you want to combine?_ ")

    answer = "y"
    while answer != "n": 
        document_name = input("Document to combine:_ ")
        document = open(document_name, "r")
        for row in document:
            combined_document.write(row)
        combined_document.write("\n")
        answer = input("Add nother one [y/n]?_ ")
    print("Done!...\n")


def check_file():
    users = []
    selected_file = input("What file do you want to check?_ ")
    
    try:
        directory_file = open(selected_file, "r")

    except IOError:
        print("ERROR: The file noes not exist...")

    else:
        for row in directory_file:
            clean_row = row.rstrip()
            l = clean_row.split(",")
            users.append(l)

    for each_user in users:
        print(each_user)


def search_record():

    selected_file = input("In what file do you want to search?_ ")
    users = []
    try:
        search = open("directory3.txt", "r")
    except IOError:
        print("ERROR: The file noes not exist...")
    else:
        for row in search:
            clean_row = row.rstrip()
            l = clean_row.split(",")
            users.append(l)

    print("""
    What do you want to display
    ____________________________ 
    [1]  Names
    [2]  Address
    [3]  Phone
    [4]  Email
    """)
    
    option_selected = int(input("Option_ ")) - 1
    count = 0

    for data in users:
        print(users[count][option_selected])
        count += 1


if __name__ == "__main__":

    print('''
    ---------------------------------------------------------------
    HI! WELLCOME TO USERDIRECTORY
    ---------------------------------------------------------------''')
    
    option = menu()

    while option != 5:

        if option == 1:
            print('''
    ---------------------------------------------------------------
    CREATING NEW RECORD
    ---------------------------------------------------------------''')
            print("\n")
            create_record()
            option = menu()
            
        elif option == 2:
            print('''
    ---------------------------------------------------------------
    COMBINE RECORDS IN A FILE
    ---------------------------------------------------------------''')
            print("\n")
            combine_records()
            option = menu()

        elif option == 3:
            print('''
    ---------------------------------------------------------------
    CHECKING RECORDS IN A FILE
    ---------------------------------------------------------------''')
            print("\n")
            check_file()
            option = menu()

        elif option == 4:
            print('''
    ---------------------------------------------------------------
    SEARCH DATA IN A RECORD
    ---------------------------------------------------------------''')
            print("\n")
            search_record()
            option = menu()

        elif option == 5:
            break

        else:
            print("ERROR: Invalid input...")

print('''
    ---------------------------------------------------------------
    GOOD BYE!
    ---------------------------------------------------------------
    ''')
