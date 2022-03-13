import WConio2  # Only works on Windows!
from console_application import authentication as auth, doctor_functions as doc
import patient_functions as patient


def app_startup():
    print("Press 'L' to login or 'C' to create a new account")
    char = WConio2.getkey()
    return char


def home(user):
    creds = user.get('credentials')
    creds_string = "Your current roles are: \n"
    for key in creds:
        if creds[key] is True:
            creds_string += ("  " + key.capitalize() + " -> Press " + key[0].capitalize() + " to access this role's "
                                                                                            "functions")
    print(creds_string)
    print("  Alternatively, enter 'E' to exit")
    exited = False
    while not exited:
        valid = False
        while not valid:
            role = WConio2.getkey()
            if role == "P":
                print("Accessing patient menu")
                patient.patient_menu(user)
                valid = True
            elif role == "D":
                print("Accessing doctor menu")
                doc.doctor_menu(user)
                valid = True
            elif role == "A":
                print("Accessing admin menu")
                valid = True
            elif role == "E":
                print("Exited")
                exited = True
            else:
                print("Invalid selection, please try again")


if __name__ == '__main__':
    print("Welcome to Justin's Healthcare App!")
    logged_in = False
    current_user = None
    while not logged_in:
        choice = app_startup()
        if choice == "L":
            logged_in = auth.login()
        elif choice == "C":
            auth.create_user()
        else:
            print("Invalid selection")

    current_user = logged_in
    print("Success")
    home(current_user.json())
