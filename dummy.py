import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "dfUwrx8irHJeNAfO7ILdsJ1nm7ZZ9olNzolpQ4skgoW4"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token',
                               data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/24837ac5-ae07-492a-a835-2de2b14f1560/predictions?version=2022-06-05', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())