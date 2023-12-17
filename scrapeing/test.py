import requests
import os

def save_api_response(url, folder_path, file_name):
    # Make the API request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Define the file path
        file_path = os.path.join(folder_path, file_name)

        # Save the JSON response to a file
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"JSON data saved to {file_path}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# API URL
api_url = "https://api.open5e.com/v1/spells/fireball"

s = len("https://api.open5e.com/v1/spells/")

# Folder to save the JSON file
save_folder = "api_data"

# File name for the JSON response
file_name = "fireball.json"

# Call the function
save_api_response(api_url, save_folder, file_name)
