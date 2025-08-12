phone_book = {}

def show_menu():
    print("\n--- PHONE DIRECTORY ---")
    print("1. View All Contacts")
    print("2. Add New Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def view_contacts():
    if not phone_book:
        print("Phone book is empty")
    else:
        for i, (contact_name, contact_number) in enumerate(phone_book.items(), 1):
            print(f"{i}. {contact_name}: {contact_number}")

def add_contact():
    contact_name = input("Enter your name: ").strip()
    contact_number = int(input("Enter your number: "))
    if (contact_name in phone_book):
        print("Contact already existed")
    else:
        phone_book[contact_name] = contact_number
        print("Contact added successfully")

def search_contact():
    search_contact =  input("Enter the name of the contact to search: ").strip()
    if (search_contact in phone_book):
        print(f"{search_contact} : {phone_book[search_contact]}")
    else:
        print("Contact not found")

def update_contact():
    update_contact = input("Enter the name of the contact to update: ")
    if (update_contact in phone_book):
        number = int(input("Enter new number: "))
        phone_book[update_contact] = number
        print("Contact updated.")
    else:   
        print("Contact new number")

def delete_contact():
    remove_contact = input("Enter the name of the contact to remove: ").strip()
    if remove_contact in phone_book:
        phone_book.pop(remove_contact)
        print("Contact deleted")
    else:
        print("Contact not found")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ").strip()

    if(choice == '1'):
        view_contacts()
    elif(choice == '2'):
        add_contact()
    elif(choice == '3'):
        search_contact()
    elif(choice == '4'):
        update_contact()
    elif(choice == '5'):
        delete_contact()
    elif(choice == '6'):
        print("GoodBye...")     
        break
    else:
        print("Invalid option. Please choose 1-6.")