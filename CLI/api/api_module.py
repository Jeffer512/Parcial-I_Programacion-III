# api/api_module.py
from sodapy import Socrata
import pandas as pd # Although pandas is imported, it's not strictly needed for returning list of dicts

def fetch_covid_data(department_name, limit_records):
    """
    Fetches COVID-19 data from the Datos Abiertos API for a given department and record limit.

    Args:
        department_name (str): The name of the department to query.
        limit_records (int): The maximum number of records to retrieve.

    Returns:
        list: A list of dictionaries, where each dictionary represents a COVID-19 case record.
              Returns None if there is an error fetching data or if no data is found.
    """
    try:
        # Unauthenticated client only works with public data sets. Note 'None'
        # in place of application token, and no username or password:
        client = Socrata("www.datos.gov.co", None)

        # Resource identifier for the "Casos positivos de COVID-19 en Colombia" dataset
        resource_id = "gt2j-8ykr"

        # Make the API request
        results = client.get(resource_id,
                                limit=limit_records,
                                departamento_nom=department_name)

        return results  # Returns a list of dictionaries

    except Exception as e:
        print(f"Error obteniendo datos desde API:: {e}")
        return None


if __name__ == '__main__':
    # Example usage to test the API module directly
    print("Testing API Module...\n")

    test_department = "SANTANDER"
    test_limit = 5

    covid_data_test = fetch_covid_data(test_department, test_limit)

    if covid_data_test:
        print(f"Successfully fetched {len(covid_data_test)} records for {test_department}:")
        for record in covid_data_test:
            # Print just a few keys from each record for brevity in testing
            print(f"  Case ID: {record.get('id_de_caso', 'N/A')}, City: {record.get('ciudad_municipio_nom', 'N/A')}, Age: {record.get('edad', 'N/A')}")
    else:
        print(f"Failed to fetch COVID-19 data for {test_department}.")