# main.py
from ui.ui_module import get_user_input, display_results
# Assuming api_module.py will be in the 'api' directory and will have a function called fetch_covid_data
from api.api_module import fetch_covid_data # Import the function from api_module

def main():
    """
    Main function to run the COVID-19 data application.
    Orchestrates user input, API data fetching, and result display.
    """
    print("Consulta Datos COVID-19!")
    print("--------------------------------------------------\n")

    department_name, limit_records = get_user_input()

    if department_name and limit_records:  # Proceed if user provided valid input
        print(f"\nObteniendo datos para el departmento: {department_name}, Limite: {limit_records} registros...\n")

        # --- Fetch data from API using the api_module ---
        covid_data = fetch_covid_data(department_name, limit_records) # Call the function from api_module

        if covid_data:
            display_results(covid_data) # Display results using ui_module
        else:
            print("Error obteniendo datos desde API.") # Handle API error or empty response

    else:
        print("Input invalido. Saliendo") # Handle case where get_user_input returned None




main()