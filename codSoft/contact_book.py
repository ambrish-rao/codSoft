# Initialize the contact dictionary
contact = {}

def display_contact():
    print("Name \t\t Contact Number \t\t E-mail \t\t\t\t Address ")

    for key, details in contact.items():
        print(f"{key} \t\t {details['phone']} \t\t {details['email']}\t\t\t {details['address']}")


while True:
    choice = int(input("1. Add new Contact \n 2. Search Contact \n 3. Display Contact \n 4. Edit Contact \n 5. Delete Contact \n 6. Exit \n Enter Your Choice :- "))

    if choice == 1:
        name = input("Enter Contact Name: ").lower()
        phone = int(input("Enter mobile Number.: "))
        email = input("Enter E-mail: ")
        address = input("Enter Address: ")
        
        # Store details as a dictionary within the contact dictionary
        contact[name] = {'phone': phone, 'email': email, 'address': address}
        

    elif choice == 2:
        search_name = input("Enter Contact Name: ").lower()

        if search_name in contact:
            details = contact[search_name]
            print(f"Name: {search_name.capitalize()}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
        else:
            print("Name is Not Found in Contact Book !")

    elif choice == 3:
        if not contact:
            print("Empty Contact Book")
        else:
            display_contact()

    elif choice == 4:
        while True:
            edit_name = input("Enter the name of the contact to edit (or type 'exit' to return to the main menu): ").lower()
            if edit_name == 'exit':
                break
            elif edit_name in contact:
                while True:
                    print("\n1. Edit Name\n2. Edit Phone\n3. Edit Email\n4. Edit Address\n5. Exit Editing")
                    edit_choice = int(input("Choose the field to edit: "))
                
                    if edit_choice == 1:
                        new_name = input("Enter new name: ").lower()
                        contact[new_name] = contact.pop(edit_name)
                        edit_name = new_name  # Update reference to new name
                    elif edit_choice == 2:
                        contact[edit_name]['phone'] = input("Enter new phone number: ")
                    elif edit_choice == 3:
                        contact[edit_name]['email'] = input("Enter new email: ")
                    elif edit_choice == 4:
                        contact[edit_name]['address'] = input("Enter new address: ")
                    elif edit_choice == 5:
                        print("Exiting editing mode.....")
                        break
                    else:
                        print("Invalid choice. Please try again.")

                    print("Contact updated successfully.\n")
            else:
                print("Name not found in contact book. Please try again.")
    elif choice == 5:
        del_contact = input("Enter  the name of the Contact to be deleted: ").lower()

        if del_contact in contact:
            confirm = input("Do you want to delete this contact Y/N ?")

            if confirm == 'Y' or confirm == 'y':
                contact.pop(del_contact)
                print("Contact Deleted..")
            display_contact()
        else:
            print("Name is not found in contact book")

    elif choice == 6:
        print("Exiting........")
        break
    else: 
        print("Invalid choice. Please try again.")