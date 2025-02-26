# ui/ui_module.py

def get_user_input():
    """
    Gets the department name and number of records from the user via console input.

    Returns:
        tuple: A tuple containing (department_name, limit_records).
               department_name is a string, and limit_records is an integer.
               Returns None if input is invalid or user cancels.
    """
    while True:
        department_name = input("Ingrese el nombre del departamento a consultar (e.g., SANTANDER): ").strip().upper()
        if not department_name:
            print("Departmento no puede estar vacio.")
            continue

        limit_records_str = input("Ingrese el maximo número de registros a obtener (e.g., 100): ").strip()
        if not limit_records_str:
            print("El número de registros no puede estar vacio.")
            continue

        try:
            limit_records = int(limit_records_str)
            if limit_records <= 0:
                print("El número de registros debe ser positivo.")
                continue
            break  # Exit loop if input is valid integer

        except ValueError:
            print("Input no valido para el número de registros. Ingrese un entero valido.")
            continue

    return department_name, limit_records


def display_results(data):
    """
    Displays the COVID-19 data in a formatted way, showing only the specified columns.

    Args:
        data:  A list of dictionaries, where each dictionary represents a COVID-19 case record.
               It's assumed that each dictionary has keys corresponding to the column names
               (e.g., 'ciudad_de_ubicacion', 'departamento', 'edad', 'tipo', 'estado', 'pais_de_procedencia').
               If data is None or empty, it displays a message indicating no results.
    """
    if not data:
        print("\nNo se encontraron casos de COVID-19 para el departamento especificado.")
        return

    # print("\nCOVID-19 Cases Data:")
    print("-" *150)  # Separator line

    # Define the columns to display and their display names (optional, for better readability)
    columns_to_display = [
        ('ciudad_municipio_nom', 'Ciudad de Ubicación'),
        ('departamento_nom', 'Departamento'),
        ('edad', 'Edad'),
        ('fuente_tipo_contagio', 'Tipo'),
        ('estado', 'Estado'),
        ('pais_viajo_1_nom', 'País de Procedencia')
    ]

    # Print header row
    header_row = ""
    for _, display_name in columns_to_display:
        header_row += f"{display_name:<25}" # Adjust width as needed, e.g., 25 characters wide
    print(header_row)
    print("-" * 150)

    # Print data rows
    for record in data:
        data_row = ""
        for column_name, _ in columns_to_display:
            value = record.get(column_name, "N/A") # Get value, default to "N/A" if column is missing
            data_row += f"{value:<25}" # Adjust width to match header
        print(data_row)

    print("-" * 150)



if __name__ == '__main__':
    # Example usage to test the UI module directly
    print("Testing UI Module...\n")

    dept_name, record_limit = get_user_input()
    print(f"\nUser Input:\nDepartment: {dept_name}, Records Limit: {record_limit}\n")

    # Example data (replace with actual data from API later)
    example_data = [
        {'ciudad_municipio_nom': 'Bucaramanga', 'departamento_nom': 'SANTANDER', 'edad': 29, 'fuente_tipo_contagio': 'Importado', 'estado': 'Leve', 'pais_viajo_1_nom': 'AFGANISTÁN'},
        {'ciudad_municipio_nom': 'Yumbo', 'departamento_nom': 'VALLE', 'edad': 44, 'fuente_tipo_contagio': 'Importado', 'estado': 'Leve', 'pais_viajo_1_nom': 'AFGANISTÁN'},
        {'ciudad_municipio_nom': 'Medellín', 'departamento_nom': 'ANTIOQUIA', 'edad': 35, 'fuente_tipo_contagio': 'Comunitaria', 'estado': 'Moderado', 'pais_viajo_1_nom': 'COLOMBIA'}
    ]

    display_results(example_data)
    display_results([]) # Test with empty data