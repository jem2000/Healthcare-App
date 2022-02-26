import WConio2  # Only works on Windows!
import datetime
import requests


def login():
    print("Logging in")
    username = input("Please enter your username: ")
    existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': username})
    if existing_name.status_code == 500:
        print("Cannot find a user with that user name, try creating a new account")
        return False
    password = input("Please enter your password: ")
    existing_account = requests.get('http://127.0.0.1:5000/authenticate', json={
        'name': username,
        'password': password})
    if existing_account.status_code == 500:
        incorrect_password = True
        while incorrect_password:
            password = input("Incorrect password, please try again or enter 'B' to go back: ")
            if password == "B":
                return False
            existing_account = requests.get('http://127.0.0.1:5000/authenticate', json={
                'name': username,
                'password': password})
            if existing_account.status_code != 500:
                incorrect_password = False
    return existing_account


def create_user():
    print("Creating new user")
    username = input("Please enter your username: ")
    existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': username})
    if existing_name.status_code != 500:
        valid = False
        while not valid:
            username = input("Name already taken, try a new name or enter 'B' to go back: ")
            existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': username})
            if username == "B":
                return False
            if existing_name.status_code == 500:
                valid = True

    password = input("Please enter your password: ")
    is_doctor = False
    is_admin = False
    is_patient = False
    finished_credentials = False
    while not finished_credentials:
        print("Select account credentials: Enter 'P' for patient, 'D' for doctor, or 'A' for admin ")
        account_type = WConio2.getkey()
        if account_type == "P" or account_type == 'D' or account_type == 'A':
            if account_type == "P":
                is_patient = True
            elif account_type == "D":
                is_doctor = True
            elif account_type == "A":
                is_admin = True
            print("Would you like to add additional credentials Y/N? ")
            additional = WConio2.getkey()
            while additional != 'Y' and additional != 'N':
                print("Try again, would you like to add additional credentials Y/N? ")
                additional = WConio2.getkey()
            if additional == 'N':
                finished_credentials = True
        else:
            print("Invalid selection, try again")
    credentials = {
        "patient": is_patient,
        "doctor": is_doctor,
        "admin": is_admin
    }
    user_info = {
        "username": username,
        "password": password,
        "credentials": credentials,
        # "devices": None,
        "health_records": [],
        "account_creation_time": datetime.datetime.utcnow().strftime('%B %d %Y')
    }

    # users.insert_one(user_info)
    requests.post('http://127.0.0.1:5000/add-new-user', json={'user_info': user_info})
    return True
