import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# Connect to the MySQL database
def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="#Hema2005",  # Your MySQL password
        database="hospital_patient_management"
    )
    return connection

# Function to add a new patient record
def add_patient():
    # Popup form for entering patient details
    def save_patient():
        name = entry_name.get()
        age = entry_age.get()
        gender = entry_gender.get()
        contact = entry_contact.get()
        diagnosis = entry_diagnosis.get()
        admission_date = datetime.now().strftime("%Y-%m-%d")
        
        conn = connect_db()
        cursor = conn.cursor()
        
        # Insert patient data into the patients table
        cursor.execute("""
            INSERT INTO patients (name, age, gender, contact, diagnosis, admission_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, age, gender, contact, diagnosis, admission_date))
        
        conn.commit()
        conn.close()
        popup.destroy()
        messagebox.showinfo("Success", "Patient record added successfully.")
    
    # Create the popup window
    popup = tk.Toplevel()
    popup.title("Add New Patient")
    
    tk.Label(popup, text="Name:").grid(row=0, column=0)
    entry_name = tk.Entry(popup)
    entry_name.grid(row=0, column=1)
    
    tk.Label(popup, text="Age:").grid(row=1, column=0)
    entry_age = tk.Entry(popup)
    entry_age.grid(row=1, column=1)
    
    tk.Label(popup, text="Gender:").grid(row=2, column=0)
    entry_gender = tk.Entry(popup)
    entry_gender.grid(row=2, column=1)
    
    tk.Label(popup, text="Contact:").grid(row=3, column=0)
    entry_contact = tk.Entry(popup)
    entry_contact.grid(row=3, column=1)
    
    tk.Label(popup, text="Diagnosis:").grid(row=4, column=0)
    entry_diagnosis = tk.Entry(popup)
    entry_diagnosis.grid(row=4, column=1)
    
    tk.Button(popup, text="Save", command=save_patient).grid(row=5, column=0, columnspan=2)
    
# Main window setup
root = tk.Tk()
root.title("Hospital Patient Management System")

# Add patient button
tk.Button(root, text="Add Patient", command=add_patient).pack(pady=10)

root.mainloop()
