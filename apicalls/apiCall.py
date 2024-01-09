import csv
import requests

# Replace with your API endpoint
api_url = 'https://mp229d025570c32d2fe8.free.beeceptor.com/mocktest'
my_headers = {'Authorization' : 'Bearer {access_token}'}

# Open and read the CSV file
#with open('api_data.csv', 'r') as csvfile:
#    csvreader = csv.reader(csvfile)

    # Assuming the CSV has a header row, skip it
 #   next(csvreader)

 #   for row in csvreader:
        # Extract data from the CSV row as needed
 #       param1 = row[0]  # Replace with the actual column index or header name
 #       param2 = row[1]  # Replace with the actual column index or header name

        # Define the payload for your API request
#        payload = {
#            'param1': param1,
#            'param2': param2,
#            # Add more parameters as needed
#        }

try:
            # Make the API request
            #response = requests.post(api_url, json=payload)
            response = requests.get(api_url,my_headers)


            # Check the response status code and handle it accordingly
    if response.status_code == 200:
            print (response.raise_for_status())
            #print("API request successful for {param1} and {param2}")
    else:
            # print(f"API request failed for {param1} and {param2}. Status code: {response.status_code}")

except Exception as e:
        print(f"Error making API request for {param1} and {param2}: {str(e)}")
except requests.exceptions.HTTPError as errh:
        print(errh)
    
except requests.exceptions.ConnectionError as errc:
        print(errc)
except requests.exceptions.Timeout as errt:
        print(errt)
except requests.exceptions.RequestException as err:
        print(err)
