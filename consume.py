"""
 REST API Consumption Problem: With the given API Url,
 write a python script to call the api with a set
 of inputs, and consume the response given.
"""


#***********Imports*************#
import requests
import json
import entryexiterrorlogging
import google.cloud.logging
import time


#********Initialize Clients***********#
logging_client = google.cloud.logging.Client()
logging_client.get_default_handler()
logging_client.setup_logging()


#**********Local Variables************#
url = "https://esldp-sit2-west.corp.cvscaremark.com:5889/DBPLService/subscription/fetchFlagPropertyValue/V1%27"
cloud_function_name = "cf-consume-response"


def consume_response():
    """
     consume_response: Function to consume a
     POST response from a REST api POST call
    """
    start_time = time.time()
    loggingdict = {"entryType" : "Subscription_Platform", "opName": cloud_function_name,
                   "src": "CVS_Cloud_Functions", "action": "CF_Consume_Respsonse", "programName": "CF_Consume_Respsonse"}

    # Invoke entry logging
    entryexiterrorlogging.entryEventLog(loggingdict, "CVSEVENT")

    try:
        # store the input of the name and type
        flag_name = input("Enter a name: ")
        type_name = input("Enter a type: ")

        # create a dictionary with these two variables as data
        input_json = {"name": flag_name, "type": type_name}

        # use dumps to convert dict into a json object
        json_request = json.dumps(input_json)

        # Initialize the headers to specified values
        headers = {
            "Accept": "application/json",
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "env": "UAT1"

        }

        # send the POST call to the url, json, and headers
        response = requests.post(url, data=json_request, headers=headers)

        # print the response of the POST call for testing
        print(response.json())

    except Exception as exe:
        # invoke error logging
        loggingdict.update({"Exception": format(exe)})
        entryexiterrorlogging.errorEventLog(loggingdict, "CVSEVENT")

    finally:
        # invoke exit logging
        resp_time = time.time() - start_time
        loggingdict.update({"respTime": str(round(resp_time, 3)) + "secs"})


# Driver Code to test above function
consume_response()
