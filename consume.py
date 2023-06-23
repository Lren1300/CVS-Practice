# *********** Imports *************#
import requests
import json

# **********Local Variables************#
url =  "https://esldp-sit2-west.corp.cvscaremark.com:5889/DBPLService/subscription/fetchFlagPropertyValue/V1%27"

# Function to consume a POST response from a REST api call

def consume_response():
    # store the input of the name and type
    flag_name = input("Enter a name: ")
    type_name = input("Enter a type: ")

    # create a json with these two variables as data
    input_json = {"name": flag_name, "type": type_name}
    json_request = json.dumps(input_json)

    # Initialize the headers
    headers = {
        "Accept": "application/json",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "env": "UAT1"

    }

    # send the POST call to the url with the given data
    response = requests.post(url, data=json_request, headers=headers)

    # print the response of the POST call
    print(response.json())

#function to call our functionality
def start_process():
    consume_response()