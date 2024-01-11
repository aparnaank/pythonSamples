import csv
import requests
import json

# Function to read data from CSV file and send API requests
def process_csv_and_send_requests(csv_file_path, api_endpoint):
    with open(csv_file_path, 'r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Assuming your CSV file has column Token.
            Token = row['Token']

            # Prepare Header for the API request
            api_header = {
                'Authorization': f'Bearer {Token}',  # Fix the syntax here
                'Content-Type': 'application/json',             
            }
           
            try:
                # Send API request
                response = send_api_request(api_endpoint, headers=api_header)

                # Process the API response (you can customize this based on your needs)
                if response.status_code == 200 : #and response.headers['Content-Type'] == 'application/json'
                    print(f"API request successful for {Token}: Status Code: {response.status_code}, Response: {response.json()}")
                else:
                    print(f"API request failed for {Token}. Status Code: {response.status_code}, Response: {response.text}")

            except requests.exceptions.RequestException as e:
                    # Handle network-related exceptions, such as connection errors or timeouts
                    print(f"Network Error: {e}")

            except requests.exceptions.HTTPError as e:
                    # Handle HTTP-related exceptions, such as 404 Not Found or 500 Internal Server Error
                    print(f"HTTP Error: {e}")

            except Exception as e:
                    # Handle other unexpected exceptionshttps://ank.requestcatcher.com/test
                    print(f"An unexpected error occurred: {e}")

# Function to send API request
def send_api_request(api_endpoint, headers):
    # Assuming it's a POST request, modify as needed
    response = requests.post(api_endpoint, headers=headers)
    return response

# Example usage
csv_file_path = '/home/aparna/pythonScripts/apicalls/api_data.csv'
api_endpoint = 'https://run.mocky.io/v3/b0521490-1b1c-4a83-94fe-abf3abbdd7e2'

# Call the function
process_csv_and_send_requests(csv_file_path, api_endpoint)

