import requests

# Define the API endpoint
api_url = 'https://api.myquran.com/v1/sholat/kota/semua'

# Send a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    for enu, item in enumerate(data):
        if item['lokasi'] == "KOTA HUMBANG HASUNDUTAN":

            print(enu, item['lokasi'])
#     # Check if the data has at least 33 items (index 32 exists)
#     if len(data) >= 33:
#         # Select and print the location at index 32
#         location_32 = data[180]
#         print(location_32)
#     else:
#         print("Index 32 does not exist in the data.")
# else:
#     print("Failed to fetch data from the API.")