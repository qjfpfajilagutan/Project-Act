import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "0S6GtCLSx9M0bozZrxF0pVNQAq617ixG"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    json_status = json_data["info"]["statuscode"]

    drt = ("{:.2f}".format(json_data["route"]["realTime"]))
    klm = ("{:.2f}".format((json_data["route"]["distance"])*1.61))
    minutes = float(drt)/60
    hr = minutes/60
    speed = float(klm)/hr

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Distance---------------------" + klm + " km")
        print("Speed of travel--------------" + str("{:.2f}".format(speed)) + " kph")
        print("Estimated Time of Arrival----" + str("{:.2f}".format(hr)) + " Hrs")
        print("=============================================")
        
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

    