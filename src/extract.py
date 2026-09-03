import requests

from logger import get_logger

obj_logger = get_logger()

def extract_users():
    # print("Starting data extraction...")
    obj_logger.info("Starting data extraction...")

    str_api_url = "https://jsonplaceholder.typicode.com/users"

    try:
        obj_response = requests.get(str_api_url, timeout=10)

        obj_response.raise_for_status() #This checks for HTTP errors

        lst_users = obj_response.json() #Convert response to JSON, Python converts it into Python list/dictionaries
        

        obj_logger.info(f"Successfully extracted {len(lst_users)} users.")

        return lst_users

    except requests.exceptions.RequestException as obj_error:
        obj_logger.error(f"Error while extracting data: {obj_error}")

        return []

