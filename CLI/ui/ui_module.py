# ui/ui_module.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from api.api_module import fetch_covid_data # Import your API function

def get_user_input(root, display_area): # Pass root and display_area
    """Sets up the GUI input elements and data fetching."""

    department_label = ttk.Label(root, text="Departamento:")
    department_label.grid(row=0, column=0, padx=5, pady=5, sticky="e") # Using grid layout

    department_entry = ttk.Entry(root)
    department_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    limit_label = ttk.Label(root, text="Limite:")
    limit_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    limit_entry = ttk.Entry(root)
    limit_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    fetch_button = ttk.Button(root, text="Obetener Datos",
                               command=lambda: fetch_and_display_data(department_entry.get().upper(), limit_entry.get(), display_area)) # Command calls a function

    fetch_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

def fetch_and_display_data(department_name, limit_records_str, display_area):
    """Fetches data from API and displays in the GUI."""
    try:
        limit_records = int(limit_records_str)
        if limit_records <= 0:
            messagebox.showerror("Input Error", "El número de registros debe ser positivo.")
            return
    except ValueError:
        messagebox.showerror("Input Error", "Input no valido para el número de registros. Ingrese un entero valido.")
        return

    data = fetch_covid_data(department_name, limit_records)
    display_results(data, display_area) # Pass display_area to display_results


def display_results(data, display_area): # Pass display_area
    """Displays results in the GUI display area using ttk.Treeview."""
    # Clear previous data from Treeview
    for item in display_area.get_children():
        display_area.delete(item)

    if not data:
        # Display a "No data found" message in the Treeview
        display_area.insert('', tk.END, values=["No se encontraron casos de COVID-19 para el departamento especificado."])
        return

    # Define columns for Treeview
    columns_to_display = [
        ('ciudad_municipio_nom', 'Ciudad de Ubicación'),
        ('departamento_nom', 'Departamento'),
        ('edad', 'Edad'),
        ('fuente_tipo_contagio', 'Tipo'),
        ('estado', 'Estado'),
        ('pais_viajo_1_nom', 'País de Procedencia')
    ]

    # Configure columns in Treeview
    display_area['columns'] = [col[0] for col in columns_to_display] # Use column names from data as IDs
    display_area['show'] = 'headings' # Hide default first column

    for col_id, col_header in columns_to_display:
        display_area.column(col_id, width=150, anchor=tk.W) # Adjust width as needed
        display_area.heading(col_id, text=col_header) # Set column header text

    # Insert data rows into Treeview
    for record in data:
        values = []
        for column_name, _ in columns_to_display:
            values.append(record.get(column_name, "N/A")) # Get values in correct order
        display_area.insert('', tk.END, values=values)


def create_ui(root): # Function to set up and return UI elements
    """Creates and arranges UI elements in the root window."""
    root.columnconfigure(1, weight=1) # Make column 1 expandable horizontally
    root.rowconfigure(3, weight=1)    # Make row 3 expandable vertically

    # Replace tk.Text with ttk.Treeview
    display_area = ttk.Treeview(root) # Create Treeview widget to show data in table format
    display_area.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

    # Add scrollbars for Treeview
    vsb = ttk.Scrollbar(root, orient="vertical", command=display_area.yview)
    vsb.grid(row=3, column=2, sticky='ns')
    display_area.configure(yscrollcommand=vsb.set)

    hsb = ttk.Scrollbar(root, orient="horizontal", command=display_area.xview)
    hsb.grid(row=4, column=0, columnspan=2, sticky='ew')
    display_area.configure(xscrollcommand=hsb.set)


    get_user_input(root, display_area) # Call get_user_input to setup input fields and button

    return root # Return the root window


if __name__ == '__main__':
    root = tk.Tk()
    root.title("COVID-19 Data Application")
    create_ui(root) # Create the UI in the root window
    root.mainloop() # Start the tkinter event loop (for testing UI module)