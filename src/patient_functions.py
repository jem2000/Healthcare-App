import WConio2  # Only works on Windows!
import pymongo
import datetime

client = pymongo.MongoClient(
    "mongodb+srv://Github:Github@cluster0.pkk8t.mongodb.net/Test1?retryWrites=true&w=majority")

db = client["Test1"]
devices = db["Devices"]
users = db["Users"]


def patient_menu(user):
    print("~-~-~-Options-~-~-~")
    print("1: View list of devices ")
    print("2: Enter new health readings")
    selection = WConio2.getkey()
    if selection == "1":
        view_devices_list(user)
        patient_menu(user)
    elif selection == "2":
        print("~-~-~-Beginning new reading-~-~-~")
        add_new_health_record(user)
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


def add_new_health_record(user):
    username = user.get('username')
    count = 1
    my_devices = []
    for device in devices.find({"user": username}, {"_id": 0, "name": 1}):
        print(count, ": ", device.get('name'))
        my_devices.append(device.get('name'))
        count += 1
    print("Select the number of the device used to create the readings")
    selection = WConio2.getkey()
    if 0 <= int(selection) - 1 < len(my_devices):
        device_name = my_devices[int(selection) - 1]
    else:
        print("Invalid selection, please try again")
        return
    print("For now, you must manually enter your values, this will be updated later!!!!!")
    bp = input("Enter blood pressure: ")
    heart_rate = input("Enter heart rate: ")
    oxygen = input("Enter blood oxygen levels: ")
    glucose = input("Enter blood glucose levels: ")
    weight = input("Enter weight: ")
    height = input("Enter height: ")

    health_reading = {
        "device_used": device_name,
        "blood_pressure": bp,
        "heart_rate": heart_rate,
        "oxygen": oxygen,
        "glucose": glucose,
        "weight": weight,
        "height": height,
        "reading_date": datetime.datetime.utcnow().strftime('%B %d %Y')
    }
    users.update_one(
        {'username': username},
        {'$push': {'health_records': health_reading}})
    print("Successfully uploaded health data")

