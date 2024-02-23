class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email: ")
        self.contacts.append(Contact(name, phone_number, email))

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}")

    def edit_contact(self):
        name = input("Enter the name of the contact you want to edit: ")
        for contact in self.contacts:
            if contact.name == name:
                phone_number = input("Enter the new phone number: ")
                email = input("Enter the new email: ")
                contact.phone_number = phone_number
                contact.email = email

    def delete_contact(self):
        name = input("Enter the name of the contact you want to delete: ")
        self.contacts = [contact for contact in self.contacts if contact.name != name]

def main():
    manager = ContactManager()
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.edit_contact()
        elif choice == "4":
            manager.delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
