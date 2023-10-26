
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox
import json
import os
from datetime import datetime

contacts = []

fenetre = tk.Tk()
fenetre.title("Gestionnaire de contacts")
fenetre.geometry("1100x1000")

selected_contact_number = tk.StringVar()

def add_contact():
    contact_name = contact_desc_entry.get()
    contact_lastname = contact_desc_entry.get()
    contact_number = contact_desc_entry.get()

    lastname_valid = bool(contact_lastname)
    name_valid = bool(contact_name)
    number_valid = bool(contact_number)

    if name_valid and number_valid and lastname_valid :
        contact = {"contact_name": contact_name, "contact_lastname": contact_lastname, "contact_number": contact_number}
        contacts.append(contact)
        update_contact_combobox()
        messagebox.showinfo("Sauvegarde", "Le contact a été ajouté avec succès.")
        
    elif not name_valid:
        messagebox.showwarning("Attention", "Veuillez entrer un prénom valide.")
    elif not lastname_valid:
        messagebox.showwarning("Attention", "Veuillez entrer un nom valide.")
    elif not number_valid:
        messagebox.showwarning("Attention", "Veuillez entrer un numéro.")


def delete_contact():
    selected_index = contact_combobox.current()
    if selected_index >= 0:
        del contact[selected_index]
        update_contact_combobox()

def save_contacts():
    file_name = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", ".json")])
    if file_name:
        with open(file_name, "w") as file:
            json.dump(contacts, file)
        messagebox.showinfo("Sauvegarde", "Les contacts ont été enregistrés avec succès.")

def load_contacts():
    file_name = filedialog.askopenfilename(filetypes=[("JSON files", ".json")])
    if file_name and os.path.exists(file_name):
        with open(file_name, "r") as file:
            global contact
            contacts = json.load(file)
        messagebox.showinfo("Chargement", "Les contacts ont été chargés avec succès.")
        update_contact_combobox()

def update_selected_contact_number(event=None):
    selected_index = contact_combobox.current()
    if selected_index >= 0:
        if len(contacts[selected_index]["contact_name"]) > 0:
          selected_contact_number.set("numéro : " + contacts[selected_index]["contact_number"] + "prénom" + contacts[selected_index]["contact_name"] + "numéro" + contacts[selected_index]["contact_number"])
        else:          
          selected_contact_number.set("Aucun numéro")
    else:
        selected_contact_number.set("Aucun contact séléctionné")

def update_contact_combobox():
    sorted_contacts = sorted(contacts, key=lambda x: x['contact_name'])  # Triez les contacts par la clé 'contact_name'
    contact_combobox['values'] = [contact["contact_name"] + contact["contact_number"] for contact in sorted_contacts]
    contact_combobox.set("")


def edit_contact():
    selected_index = contact_combobox.current()
    if selected_index >= 0:
        edited_name = edited_name_entry.get()
        edited_number = edited_number_entry.get()

        if edited_name and edited_number:
            contacts[selected_index]["contact_name"] = edited_name
            contacts[selected_index]["contact_number"] = edited_number
            update_contact_combobox()
            messagebox.showinfo("Modification", "Le contact a été modifié avec succès.")
        else:
            messagebox.showwarning("Attention", "Veuillez entrer un nom et un numéro valides.")
    else:
        messagebox.showwarning("Attention", "Aucun contact sélectionné.")

def update_selected_contact_number(event=None):
    selected_index = contact_combobox.current()
    if selected_index >= 0:
        selected_contact = contacts[selected_index]
        selected_contact_number.set("Numéro : " + selected_contact["contact_name"])

        # Affiche les valeurs actuelles dans les champs de modification
        edited_name_entry.delete(0, tk.END)
        edited_name_entry.insert(0, selected_contact["contact_name"])
        edited_number_entry.delete(0, tk.END)
        edited_number_entry.insert(0, selected_contact["contact_number"])
    else:
        selected_contact_number.set("Aucun contact sélectionné")

add_label = tk.Label(fenetre, text="Détail :",font=8)
add_label.place(x=450,y=42)

add_label = tk.Label(fenetre, text="Sélectionner un contact",font=55)
add_label.place(x=350,y=0)

add_label = tk.Label(fenetre, text="Ajoutez un contact",font=55)
add_label.place(x=350,y=120)

add_label = tk.Label(fenetre, text="Modifier un contact",font=55)
add_label.place(x=350,y=370)

contact_name_label = tk.Label(fenetre, text="Nom du contact:", font=35)
contact_name_label.place(x=40,y=150)

contact_combobox = Combobox(fenetre, width=50)
contact_combobox.place(x=100,y=50)

contact_combobox.bind("<<ComboboxSelected>>", update_selected_contact_number)

update_selected_contact_number()

selected_contact_label = tk.Label(fenetre, textvariable=selected_contact_number, bg="white")
selected_contact_label.place(x=550,y=50)

delete_button = tk.Button(fenetre, text="Supprimer", command=delete_contact, font=35)
delete_button.place(x=750,y=40)

contact_number_label = tk.Label(fenetre, text="son numéro:", font=35)
contact_number_label.place(x=50,y=200)

detail_desc_entry = tk.Entry(fenetre, width=60)
detail_desc_entry.place(x=200,y=150)

add_button = tk.Button(fenetre, text="Ajouter le contact", command=add_contact, font=35)
add_button.place(x=250,y=250)

contact_desc_entry = tk.Entry(fenetre, width=60)
contact_desc_entry.place(x=200,y=200)

load_button = tk.Button(fenetre, text="Charger une liste de contacts", command=load_contacts, font=35)
load_button.place(x=50,y=600)

save_button = tk.Button(fenetre, text="Enregistrer les contacts dans un ficher", command=save_contacts, font=35)
save_button.place(x=350,y=600)



edited_name_label = tk.Label(fenetre, text="Nouveau nom:", font=("Arial", 14))
edited_name_label.place(x=50, y=400)

edited_name_entry = tk.Entry(fenetre, width=40)
edited_name_entry.place(x=200, y=400)

edited_number_label = tk.Label(fenetre, text="Nouveau numéro:", font=("Arial", 14))
edited_number_label.place(x=50, y=450)

edited_number_entry = tk.Entry(fenetre, width=40)
edited_number_entry.place(x=200, y=450)

edit_button = tk.Button(fenetre, text="Modifier", command=edit_contact, font=("Arial", 14))
edit_button.place(x=250, y=500)






fenetre.mainloop()