import WConio2  # Only works on Windows!
import datetime
import requests


def start_new_convo(user):
    recipient_name = input("Enter the username of the person you want to start a conversation with: ")
    existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': recipient_name})
    if existing_name.status_code == 500:
        valid = False
        while not valid:
            print("Cannot find a user with that user name, try creating a new account")
            recipient_name = input("Enter the username of the person you want to start a conversation with or B to go back: ")
            existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': recipient_name})
            if recipient_name == "B":
                return False
            if existing_name.status_code != 500:
                valid = True

    participants = (user.get('username'), recipient_name)
    existing_conv = requests.get('http://127.0.0.1:5000/view-messages', json={'participants': participants})

    if existing_conv.status_code != 500 and existing_conv.status_code != 200:
        valid = False
        while not valid:
            recipient_name = input("This conversation already exists, select another user or press B to go back: ")
            conv_participants = (user.get('username'), recipient_name)
            participants = frozenset(conv_participants)
            existing_conv = requests.get('http://127.0.0.1:5000/view-messages', json={'participants': participants})
            if recipient_name == "B":
                return False
            if existing_conv.status_code == 500:
                valid = True
    message = input("Enter a message to begin the conversation: ")
    message_dict = {
        "content": message,
        "timestamp": datetime.datetime.utcnow().strftime('%B %d %Y')
    }

    new_conversation = {
        "participants": participants,
        "messages": [message_dict]
    }

    requests.post('http://127.0.0.1:5000/start-new-conversation', json=new_conversation)
