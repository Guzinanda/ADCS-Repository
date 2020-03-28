'''
@ TITLE:    Catalog.py
@ DATE:     25-03-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Exercise 20
'''

class User:
    name = None
    email = None
    age = None
    country_of_origin = None

    def __init__(self, name, email, age, country_of_origin):
        self.name = name
        self.email = email
        self.age = age
        self.country_of_origin


class Catalog:
    users = []

    def __init__(self):
        pass
    
    def add_record(self, user):
        self.users.append(user)
        pass

    def list_records(self):
        print("List of records found")
        for user in self.users:
            print("Username: {0},\t email: {1},\t age: {2},\t country: {3}".format(user.name, user.email, user.age, user.country_of_origin))
        print("---------")
        pass

    def look_for_record(self, mail, age):
        for user in self.users:
            if user.email == mail and user.age == age:
                print("Record Found! \n Username: {0},\t email: {1},\t age: {2},\t country: {3}".format(user.name, user.email, user.age, user.country_of_origin))
        print("---------")
        pass

    def delete_record(self, mail, age):
        for user in self.users:
            if user.email == mail and user.age == age:
                self.users.remove(user)
        pass

    def write_to_file(self):
        if not self.users:
            return
        with open("output.txt", "w") as txt_file:
            for user in self.users:
                txt_file.write("Username: {0},\t email: {1},\t age: {2},\t country: {3}".format(user.name, user.email, user.age, user.country_of_origin) + "\n") # works with any number of elements in a line


def main():

    first_user = User("Fernanda", "guzinanda@intel.com", 26, "mexico")
    second_user = User("edgar", "edgar@oracle.com", 28, "mexico")

    my_catalog = Catalog()
    my_catalog.add_record(first_user)
    my_catalog.add_record(second_user)
    my_catalog.list_records()
    my_catalog.look_for_record("edgar@oracle.com",28)
    my_catalog.delete_record("edgar@oracle.com",28)
    my_catalog.list_records()
    my_catalog.write_to_file()


if __name__ == "__main__":
    main()
