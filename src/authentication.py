import WConio2  # Only works on Windows!
import pymongo
import datetime

client = pymongo.MongoClient(
    "")

db = client["Test1"]
col = db["Collection1"]


def login():
    print("Logging in")
    username = input("Please enter your username: ")
    existing_name = col.find_one({'username': username})
    if existing_name is None:
        print("Cannot find a user with that user name, try creating a new account")
        return False
    password = input("Please enter your password: ")
    existing_account = col.find_one({'username': username, 'password': password})
    if existing_account is None:
        incorrect_password = True
        while incorrect_password:
            password = input("Incorrect password, please try again or enter 'B' to go back: ")
            if password == "B":
                return False
            existing_account = col.find_one({'username': username}, {'password': password})
            if existing_account is not None:
                incorrect_password = False
    else:
        return existing_account


def create_user():
    print("Creating new user")
    username = input("Please enter your username: ")
    existing_name = col.find_one({'username': username})
    if existing_name is not None:
        valid = False
        while not valid:
            username = input("Name already taken, try a new name or enter 'B' to go back: ")
            existing_name = col.find_one({'username': username})
            if username == "B":
                return False
            if existing_name is None:
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
        "account_creation_time": datetime.datetime.utcnow().strftime('%B %d %Y')
    }

    col.insert_one(user_info)

    return True
