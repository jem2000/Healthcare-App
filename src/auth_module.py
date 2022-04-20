import datetime

name_dict = {
    "name": ""
}

new_user_dict = {
    "username": "",
    "password": "",
    "credentials": {},
    "health_records": [],
    "account_creation_time": datetime.datetime.utcnow().strftime('%B %d %Y')
}

creds_dict = {
    "patient": False,
    "doctor": False,
    "admin": False
}


def check_find_username(user):
    if user.keys() != name_dict.keys():
        return "Incorrect name format"
    elif isinstance(user["name"], str) is False:
        return "Name must be a string"
    else:
        return True


def check_new_user(new_user):
    if new_user.keys() != new_user_dict.keys():
        return "Incorrect user format"
    elif isinstance(new_user["username"], str) is False or isinstance(new_user["password"], str) is False:
        return "Username and password must be strings"
    elif check_credentials(new_user["credentials"]) is not True:
        return "Invalid user credentials"
    else:
        return True


def check_credentials(user_creds):
    if user_creds.keys() != creds_dict.keys():
        return "Credential keys unrecognized"
    elif isinstance(user_creds["patient"], bool) is False or isinstance(user_creds["patient"], bool) is False or \
            isinstance(user_creds["patient"], bool) is False:
        return "Credentials must be of type bool"
    else:
        return True
