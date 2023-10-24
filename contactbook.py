import tkinter as tk
from tkinter import messagebox
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields!")
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")
def search_contact():
    query = search_entry.get()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if query.lower() in name.lower() or query in details['Phone']:
            contact_list.insert(tk.END, f"{name} - {details['Phone']}")
def update_selected_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        phone = contacts[name]['Phone']
        email = contacts[name]['Email']
        address = contacts[name]['Address']

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        name_entry.insert(0, name)
        phone_entry.insert(0, phone)
        email_entry.insert(0, email)
        address_entry.insert(0, address)
def delete_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        del contacts[name]
        update_contact_list()
        clear_entries()
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
contacts = {}

# Create a tkinter window
root = tk.Tk()
root.title("Contact Book")

# Create and configure GUI elements
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

contact_list = tk.Listbox(root)
contact_list.pack()

view_button = tk.Button(root, text="View Contact", command=update_selected_contact)
view_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

root.mainloop()
