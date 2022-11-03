from tkinter import *
from tkinter import messagebox
import urllib.parse
import requests



main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "0S6GtCLSx9M0bozZrxF0pVNQAq617ixG"



def submit():
    location=entry1.get()
    destination=entry2.get()



    url = main_api + urllib.parse.urlencode({"key": key, "from":location, "to":destination})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]





    drt = ("{:.2f}".format(json_data["route"]["realTime"]))
    klm = ("{:.2f}".format((json_data["route"]["distance"])*1.61))
    minutes = float(drt)/60
    hr = minutes/60
    speed = float(klm)/hr





    if json_status == 0:
        ml1 = Label(root,text="API Status: " + str(json_status) + " = A successful route call.\n", fg = "violet",font = "Arial" ).place(x=20,y=160)
        ml2 = Label(root,text="Directions from " + (location + " to " + (destination)),fg = "violet",font = "Arial").place(x=20,y=200)
        ml3 = Label(root,text="Distance: " +  klm + " km", fg = "violet",font = "Arial").place(x=20,y=240)
        ml4 = Label(root,text="Speed of travel: " + str("{:.2f}".format(speed)) + " kph", fg = "violet",font = "Arial").place(x=20,y=280)
        ml5 = Label(root,text="Estimated Time of Arrival " + str("{:.2f}".format(hr)) + " Hrs", fg = "violet",font = "Arial").place(x=20,y=320)

            

    else:
        messagebox.showinfo("","Unknown Information!")

    






root=Tk()
root.title("Group 4 Project activity4")
root.geometry("400x400")





global entry1
global entry2



Label(root,text="Location", fg = "violet",font = "Arial").place(x=20,y=20)
Label(root,text="Destination", fg="violet",font = "Arial").place(x=20,y=60)


entry1=Entry(root,bd=1)
entry1.place(x=150,y=20)



entry2=Entry(root,bd=1)
entry2.place(x=150,y=60)



Button(root,text="Submit",command=submit,height=1,width=15,bd=5, fg ="violet",font = "Arial").place(x=150,y=100)


root.mainloop()
