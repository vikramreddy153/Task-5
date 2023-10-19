contacts = {}

def add_contact(name, phone, email, address):
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")

def search_contact(query):
    results = []
    for name, details in contacts.items():
        if query in name or query in details['Phone']:
            results.append((name, details))
    return results

def update_contact(name, phone, email, address):
    if name in contacts:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        query = input("Enter a name or phone number to search: ")
        results = search_contact(query)
        if results:
            print("Search Results:")
            for name, details in results:
                print(f"Name: {name}, Phone: {details['Phone']}")
        else:
            print("No results found.")
    elif choice == "4":
        name = input("Enter the name of the contact to update: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        update_contact(name, phone, email, address)
    elif choice == "5":
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
