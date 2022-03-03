import WConio2  # Only works on Windows!
import datetime
import requests
import message_functions as msg


def doctor_menu(user):
    print("Press 1 to register new device or B to go back")
    print("3: Start new conversation")
    print("4: View conversations")
    print("5: Send new message")
    selection = WConio2.getkey()
    if selection == "1":
        register_new_device(user)
        doctor_menu(user)
    elif selection == "3":
        print("~-~-~-Starting new conversation-~-~-~")
        msg.start_new_convo(user)
        doctor_menu(user)
    elif selection == "4":
        print("~-~-~-Viewing conversations-~-~-~")
        msg.view_conversations(user)
        doctor_menu(user)
    elif selection == "5":
        print("~-~-~-Sending new message-~-~-~")
        msg.send_message(user, None)
        doctor_menu(user)
    elif selection == "B":
        return
    else:
        print("Invalid selection, please try again")
        doctor_menu(user)


def register_new_device(user):
    device_type = input("Enter device type: ")

    device_name = input("Enter device name: ")
    existing_name = requests.get('http://127.0.0.1:5000/find-device', json={'name': device_name})
    if existing_name.status_code != 500:
        valid = False
        while not valid:
            device_name = input("Name already taken, try a new name or enter 'B' to go back: ")
            existing_name = requests.get('http://127.0.0.1:5000/find-device', json={'name': device_name})
            if device_name == "B":
                return False
            if existing_name.status_code == 500:
                valid = True

    device_user = input("Enter device user: ")

    device_MAC = input("Enter device MAC address: ")
    existing_MAC = requests.get('http://127.0.0.1:5000/find-device', json={'MAC': device_MAC})
    if existing_MAC.status_code != 500:
        valid = False
        while not valid:
            device_MAC = input("MAC already taken, try a different device or enter 'B' to go back: ")
            existing_MAC = requests.get('http://127.0.0.1:5000/find-device', json={'MAC': device_MAC})
            if device_MAC == "B":
                return False
            if existing_MAC.status_code == 500:
                valid = True

    new_device = {"device": {
        "type": device_type,
        "name": device_name,
        "user": device_user,
        "assignee": user.get('username'),
        "MAC": device_MAC,
        "registration_date": datetime.datetime.utcnow().strftime('%B %d %Y')
        }
    }

    requests.post('http://127.0.0.1:5000/add-new-device', json=new_device)
