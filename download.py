import requests
import json
import os








# def startDownload(num):
#     # API endpoint URL
#     api_url = "https://open-api.my.id/api/quran/surah/" + str(num)

#     # Send a GET request to the API
#     response = requests.get(api_url)

#     # Check the response status code
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = response.json()
        
#         # Create a folder if it doesn't exist
#         folder_path = "dataSurah"
#         os.makedirs(folder_path, exist_ok=True)
        
#         # Define the file path for saving the JSON data
#         file_path = os.path.join(folder_path, str(str(num) + ".json"))
        
#         # Save the JSON data to a file
#         with open(file_path, "w") as json_file:
#             json.dump(data, json_file, indent=4)
        
#         print(f"JSON data saved to {file_path}")
#     else:
#         print(f"Request failed with status code {response.status_code}")



# for i in range(1, 115):
#     startDownload(i)
#     print(f"Downloading surah {i}...")
#     print("Done!")



def jusDownload():
    # API endpoint URL
    api_url = "https://api.quran.com/api/v4/juzs"

    # Send a GET request to the API
    response = requests.get(api_url)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Create a folder if it doesn't exist
        folder_path = "juzz"
        os.makedirs(folder_path, exist_ok=True)
        
        # Define the file path for saving the JSON data
        file_path = os.path.join(folder_path, str(".json"))
        
        # Save the JSON data to a file
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"JSON data saved to {file_path}")
    else:
        print(f"Request failed with status code {response.status_code}")



jusDownload()
print("Done!")