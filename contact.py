import tkinter as tk
from tkinter import messagebox

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Contacts dictionary to store contact details
        self.contacts = {}

        # Create GUI elements
        self.name_frame = tk.Frame(root)
        self.name_frame.pack(fill=tk.BOTH, expand=True)
        self.name_label = tk.Label(self.name_frame, text="Name:", bg='black', fg='yellow')
        self.name_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.name_entry = tk.Entry(self.name_frame)
        self.name_entry.pack(side=tk.RIGHT, padx=5, pady=5)

        self.phone_frame = tk.Frame(root)
        self.phone_frame.pack(fill=tk.BOTH, expand=True)
        self.phone_label = tk.Label(self.phone_frame, text="Phone Number:",bg='black', fg='yellow')
        self.phone_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.phone_frame)
        self.phone_entry.pack(side=tk.RIGHT, padx=5, pady=5)

        self.email_frame = tk.Frame(root)
        self.email_frame.pack(fill=tk.BOTH, expand=True)
        self.email_label = tk.Label(self.email_frame, text="Email:",bg='black', fg='yellow')
        self.email_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.email_entry = tk.Entry(self.email_frame)
        self.email_entry.pack(side=tk.RIGHT, padx=5, pady=5)

        self.address_frame = tk.Frame(root)
        self.address_frame.pack(fill=tk.BOTH, expand=True)
        self.address_label = tk.Label(self.address_frame, text="Address:",bg='black', fg='yellow')
        self.address_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.address_entry = tk.Entry(self.address_frame)
        self.address_entry.pack(side=tk.RIGHT, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Contact",bg='black', fg='yellow', command=self.add_contact)
        self.add_button.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.view_button = tk.Button(root, text="View Contacts",bg='black', fg='yellow', command=self.view_contacts)
        self.view_button.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.search_frame = tk.Frame(root)
        self.search_frame.pack(fill=tk.BOTH, expand=True)
        self.search_label = tk.Label(self.search_frame, text="Search:",bg='black', fg='yellow')
        self.search_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.search_button = tk.Button(self.search_frame, text="Search",bg='black', fg='yellow', command=self.search_contact)
        self.search_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.remove_frame = tk.Frame(root)
        self.remove_frame.pack(fill=tk.BOTH, expand=True)
        self.remove_label = tk.Label(self.remove_frame, text="Remove Contact:",bg='black', fg='yellow')
        self.remove_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.remove_entry = tk.Entry(self.remove_frame)
        self.remove_entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.remove_button = tk.Button(self.remove_frame, text="Remove", bg='black', fg='yellow',command=self.remove_contact)
        self.remove_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"Name: {name}, Phone: {details['Phone']}" for name, details in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        query = self.search_entry.get()
        if query:
            found_contacts = []
            for name, details in self.contacts.items():
                if query.lower() in name.lower() or query in details['Phone']:
                    found_contacts.append(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            if found_contacts:
                contact_info = "\n".join(found_contacts)
                messagebox.showinfo("Search Results", contact_info)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search query.")

    def remove_contact(self):
        name_to_remove = self.remove_entry.get()
        if name_to_remove in self.contacts:
            del self.contacts[name_to_remove]
            messagebox.showinfo("Success", f"Contact '{name_to_remove}' removed successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
