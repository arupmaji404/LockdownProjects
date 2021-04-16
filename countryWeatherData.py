from tkinter import *
import requests
import json

root = Tk()

countryCode_label = Label(root, text = "Enter Country Code: ").grid(row = 0, column = 0, padx = 10, pady = 10)
zipCode_label = Label(root, text = "Enter Zip Code: ").grid(row = 1, column = 0, padx = 10, pady = 10)

countryCode_input = Entry(root, width = 50)
zipCode_input = Entry(root, width = 50)
countryCode_input.grid(row = 0, column = 1, padx = 10, pady = 10)
zipCode_input.grid(row = 1, column = 1, padx = 10, pady = 10)

def clicked():
    global countryCode_input
    global zipCode_input
    # api_requests = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=713304,in&appid=b6972e10797e77dbb75970f690b01332")
    api_requests = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + zipCode_input.get() + "," + countryCode_input.get() + "&appid=b6972e10797e77dbb75970f690b01332")
    api = json.loads(api_requests.content)
    i = 0
    status = Tk()
    for item in api:
        # print(item)
        Label(status, text = item).grid(row = i, column = 0, padx = 10)
        Label(status, text = api[item]).grid(row = i, column = 1, padx = 10)
        i += 1

Button(root, text = "Show Details", command = clicked).grid(row = 2, padx = 20, columnspan = 2)

"""
try:
    api_requests = requests.get("api.openweathermap.org/data/2.5/weather?zip=713334,+91&appid=b6972e10797e77dbb75970f690b01332")
    api = json.loads(api_requests.content)
except Exception as e:
    api = "Error"
"""

root.mainloop()    