import WConio2  # Only works on Windows!
import datetime
import requests


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
    device_list = requests.get('http://127.0.0.1:5000/view-devices', json={'name': username}).json()
    print(device_list)


def add_new_health_record(user):
    username = user.get('username')
    count = 1
    device_list = requests.get('http://127.0.0.1:5000/view-devices', json={'name': username}).json()
    for device in device_list:
        print(count, ": ", device.get('name'))
        count += 1
    print("Select the number of the device used to create the readings")
    selection = WConio2.getkey()
    if 0 <= int(selection) - 1 < len(device_list):
        device_name = device_list[int(selection) - 1]
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
    requests.post('http://127.0.0.1:5000/new-reading', json={
        'name': username,
        'health_reading': health_reading
    })

    print("Successfully uploaded health data")

