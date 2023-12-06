from DataHRS import DataHRS
data_hrs = DataHRS() 

def display_menu():
    print("Main Menu")
    print("1. Add New Patient")
    print("2. Update Patient Details")
    print("3. Search for a patient")
    print("4. Exit")

def option1():
    data_hrs.add_user()

def option2():
    update_patient_menu()
def option3():
    data_hrs.search_user()

def update_patient_menu():
    while True:
        print("Update Patient Details:")
        print("1. Update last name")
        print("2. Update first name")
        print("3. Back")


        choice = input("Enter your choice: ")

        if choice == "1":
            data_hrs.update_patient_last()

        elif choice == "2":
            data_hrs.update_patient_first()

        elif choice == "3":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
