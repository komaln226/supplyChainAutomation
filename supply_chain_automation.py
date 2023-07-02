import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

# Function to automate the supply chain tasks
def automate_tasks():
    # Open file dialog to select the supply chain data file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if file_path:
        try:
            # Read the supply chain data from the selected file
            data = pd.read_csv(file_path)
            
            # Perform the required automation tasks on the data
            # Example tasks:
            # - Calculate total transaction time
            transaction_time = data['End Time'] - data['Start Time']
            data['Transaction Time'] = transaction_time
            
            # - Optimize inventory management
            data['Inventory Status'] = ['High' if qty > 100 else 'Low' for qty in data['Quantity']]
            
            # Show a message box with the results
            messagebox.showinfo("Automation Result", "Tasks have been automated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "No file selected!")

# Create the main application window
window = tk.Tk()
window.title("Supply Chain Automation Tool")

# Create a label
label = tk.Label(window, text="Welcome to the Supply Chain Automation Tool!", font=("Arial", 14))
label.pack(pady=20)

# Create a button to trigger automation
button = tk.Button(window, text="Automate Tasks", command=automate_tasks, font=("Arial", 12))
button.pack(pady=10)

# Start the main event loop
window.mainloop()