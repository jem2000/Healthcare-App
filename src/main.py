import WConio2  # Only works on Windows!
import authentication as auth


def app_startup():
    print("Press 'L' to login or 'C' to create a new account")
    char = WConio2.getkey()
    return char


if __name__ == '__main__':
    print("Welcome to Justin's Healthcare App!")
    logged_in = False
    while not logged_in:
        choice = app_startup()
        if choice == "L":
            logged_in = auth.login()
        elif choice == "C":
            logged_in = auth.create_user()
        else:
            print("Invalid selection")
            app_startup()
        if logged_in is False:
            print("Authentication failed ")
