import requests
import json


def make_api_get_requests(api_url, num_requests=10):
    # Prepare Header for the API request
    api_header = {
        'Authorization': 'Bearer d974c5e5-41f8-39ec-b216-992ae6a355c1',
        'Content-Type': 'application/json',             
    }

    for _ in range(num_requests):

        try:
            # Send a GET request to the API
            response = requests.get(api_url, headers=api_header)

            # Check if the rsponse status code is successful (e.g., 200 OK)
            if response.status_code == 200:
            # API request was successful, process the response data
                data = response.json()
                print("Content-Type:",response.headers.get("Content-Type"))
                #print("Status Code :",response.status_code)
                #print("API Response:",data)
                print(f"Request { _ + 1 }: Status Code :{response.status_code} - Successful Response - {response.json()} ")

            else:
                # Handle non-successful response status codes
                #print(f"API Request failed with status code {response.status_code}")
                print(f"Request { _ + 1 }: Error - Status Code: {response.status_code}")
                print(f"Request {request_number + 1}: Error - Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Handle network-related exceptions, such as connection errors or timeouts
            print(f"Network Error: {e}")

        except requests.exceptions.HTTPError as e:
            # Handle HTTP-related exceptions, such as 404 Not Found or 500 Internal Server Error
            print(f"HTTP Error: {e}")

        except Exception as e:
            # Handle other unexpected exceptions
            print(f"An unexpected error occurred: {e}")
            print(f"Raw Response Content: {response.text}")


def make_api_post_requests(api_url, num_requests=10):
    # Prepare Header for the API request
    api_header = {
        'Authorization': 'Bearer d974c5e5-41f8-39ec-b216-992ae6a355c1',
        'Content-Type': 'application/json',             
    }

    for _ in range(num_requests):

        try:
            # Send a POST request to the API
            response = requests.post(api_url, headers=api_header)

            # Check if the rsponse status code is successful (e.g., 200 OK)
            if response.status_code == 200:
            # API request was successful, process the response data
                data = response.json()
                print("Content-Type:",response.headers.get("Content-Type"))
                #print("Status Code :",response.status_code)
                #print("API Response:",data)
                print(f"Request { _ + 1 }: Status Code :{response.status_code} - Successful Response - {response.json()} ")

            else:
                # Handle non-successful response status codes
                #print(f"API Request failed with status code {response.status_code}")
                print(f"Request { _ + 1 }: Error - Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Handle network-related exceptions, such as connection errors or timeouts
            print(f"Network Error: {e}")

        except requests.exceptions.HTTPError as e:
            # Handle HTTP-related exceptions, such as 404 Not Found or 500 Internal Server Error
            print(f"HTTP Error: {e}")

        except Exception as e:
            # Handle other unexpected exceptions
             print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Replace 'https://example.com/api' with the actual API endpoint you want to request
    # api_endpoint = 'http://localhost:5000/testEP/get_request'
    api_endpoint = 'https://run.mocky.io/v3/b0521490-1b1c-4a83-94fe-abf3abbdd7e2'

    # Specify the number of times you want to make the request (default is 100)
    num_requests = 5

    # Call the function
    make_api_get_requests(api_endpoint, num_requests)
    make_api_post_requests(api_endpoint, num_requests)