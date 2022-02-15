import WConio2  # Only works on Windows!
import pymongo
import datetime

client = pymongo.MongoClient(
    "mongodb+srv://Github:Github@cluster0.pkk8t.mongodb.net/Test1?retryWrites=true&w=majority")

db = client["Test1"]
devices = db["Devices"]
users = db["Users"]


def patient_menu(user):
    print("Press 1 to view list of devices ")
    selection = WConio2.getkey()
    if selection == "1":
        view_devices_list(user)
        patient_menu(user)
    elif selection == "B":
        return
    else:
        print("Invalid selection, please try again")
        patient_menu(user)


def view_devices_list(user):
    username = user.get('username')
    for device in devices.find({"user": username}, {"_id": 0, "name": 1}):
        print(device.get('name'))
