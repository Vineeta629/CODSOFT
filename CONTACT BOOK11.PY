import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

# Function to display all contacts
def display_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_info = "Name: " + contact['name'] + " | Phone: " + contact['phone']
        contact_list.insert(tk.END, contact_info)

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        display_contacts()
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to search for a contact
def search_contact():
    query = search_entry.get().lower()
    if query:
        search_result = [contact for contact in contacts if
                         query in contact['name'].lower() or query in contact['phone']]
        if search_result:
            contact_list.delete(0, tk.END)
            for contact in search_result:
                contact_info = ("Name: " + contact['name'] + " | Phone: " + contact['phone'] + " | Email: "
                                + contact['email'] + " | Address: " + contact['address'])
                contact_list.insert(tk.END, contact_info)
        else:
            messagebox.showinfo("No Result", "No matching contact found.")
    else:
        display_contacts()

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        del contacts[index]
        display_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

# Function to update a contact
def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        contact = contacts[index]
        new_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact['name'])
        new_phone = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contact['phone'])
        new_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact['email'])
        new_address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact['address'])
        contact['name'] = new_name if new_name else contact['name']
        contact['phone'] = new_phone if new_phone else contact['phone']
        contact['email'] = new_email if new_email else contact['email']
        contact['address'] = new_address if new_address else contact['address']
        display_contacts()
        messagebox.showinfo("Success", "Contact updated successfully.")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")

# Create main window
root = tk.Tk()
root.title("Contact Book")
root.configure(background="lightyellow")

heading = tk.Label(root, text="Contact Book", font=("Kristen ITC",20,"bold","underline"), bg="lightyellow", fg="darkgreen")
heading.pack(pady=10)

# Create frames
add_frame = tk.Frame(root, padx=20, pady=20, bg="lightyellow")
add_frame.pack(padx=10, pady=10)

search_frame = tk.Frame(root, padx=20, pady=20, bg="lightyellow")
search_frame.pack(padx=10, pady=10)

list_frame = tk.Frame(root, padx=20, pady=20, bg="lightyellow")
list_frame.pack(padx=10, pady=10)

# Add contact frame widgets
tk.Label(add_frame, text="Name:", bg="lightyellow", font=("Arial",15)).grid(row=0, column=0)
name_entry = tk.Entry(add_frame)
name_entry.grid(row=0, column=1)

tk.Label(add_frame, text="Phone Number:", bg="lightyellow", font=("Arial",15)).grid(row=1, column=0)
phone_entry = tk.Entry(add_frame)
phone_entry.grid(row=1, column=1)

tk.Label(add_frame, text="Email:", bg="lightyellow", font=("Arial",15)).grid(row=2, column=0)
email_entry = tk.Entry(add_frame)
email_entry.grid(row=2, column=1)

tk.Label(add_frame, text="Address:", bg="lightyellow", font=("Arial",15)).grid(row=3, column=0)
address_entry = tk.Entry(add_frame)
address_entry.grid(row=3, column=1)

add_button = tk.Button(add_frame, text="Add Contact", command=add_contact, font=("Arial",15), bg="deeppink", fg="white")
add_button.grid(row=4, columnspan=2, pady=10)

update_button = tk.Button(add_frame, text="Update Contact", command=update_contact, font=("Arial",15), bg="blueviolet", fg="white")
update_button.grid(row=5, columnspan=2, pady=10)

# Search frame widgets
tk.Label(search_frame, text="Search by Name or Phone Number:", bg="lightyellow", font=("Arial",15)).grid(row=0, column=0)
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1)

search_button = tk.Button(search_frame, text="Search", command=search_contact, font=("Arial",15), bg="blue", fg="white")
search_button.grid(row=0, column=2, padx=10)

reset_button = tk.Button(search_frame, text="Reset", command=display_contacts, font=("Arial",15), bg="orange", fg="white")
reset_button.grid(row=0, column=3, padx=10)

# Contact list frame widgets
contact_list = tk.Listbox(list_frame, width=100, height=12)
contact_list.grid(row=0, column=0, columnspan=2)

delete_button = tk.Button(list_frame, text="Delete", command=delete_contact, font=("Arial",15), bg="red", fg="white")
delete_button.grid(row=1, column=0,columnspan=4, pady=10)

display_contacts()

root.mainloop()