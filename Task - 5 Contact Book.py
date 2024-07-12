# Task - 5 Contact Book

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contacts(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        return results

    def update_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
        else:
            print("Invalid contact index!")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
        else:
            print("Invalid contact index!")

# Main program loop
contact_list = ContactList()

while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact_list.add_contact(Contact(name, phone, email, address))
        print("Contact added successfully.")
    elif choice == '2':
        contact_list.view_contacts()
    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        results = contact_list.search_contacts(query)
        if results:
            for idx, contact in enumerate(results, 1):
                print(f"{idx}. {contact.name} - {contact.phone}, {contact.email}, {contact.address}")
        else:
            print("No matching contacts found.")
    elif choice == '4':
        contact_list.view_contacts()
        try:
            index = int(input("Enter the index of the contact to update: ")) - 1
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_list.update_contact(index, Contact(name, phone, email, address))
            print("Contact updated successfully.")
        except (ValueError, IndexError):
            print("Invalid input or index. Please enter a valid index.")
    elif choice == '5':
        contact_list.view_contacts()
        try:
            index = int(input("Enter the index of the contact to delete: ")) - 1
            contact_list.delete_contact(index)
            print("Contact deleted successfully.")
        except (ValueError, IndexError):
            print("Invalid input or index. Please enter a valid index.")
    elif choice == '6':
        print("Exiting the contact manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")