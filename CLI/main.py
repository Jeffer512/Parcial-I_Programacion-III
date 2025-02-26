# main.py
import tkinter as tk
from ui.ui_module import create_ui # Import create_ui instead of get_user_input, display_results

def main():
    root = tk.Tk() # Create main tkinter window in main.py
    root.title("Consulta Datos COVID-19")
    create_ui(root) # Call create_ui to set up the UI in the root window
    root.mainloop() # Start the tkinter event loop in main.py

main()