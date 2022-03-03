import WConio2  # Only works on Windows!
import datetime
import requests


def start_new_convo(user):
    username = user.get('username')
    recipient_name = input("Enter the username of the person you want to start a conversation with: ")
    existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': recipient_name})
    if existing_name.status_code == 500:
        valid = False
        while not valid:
            print("Cannot find a user with that user name")
            recipient_name = input("Enter the username of the person you want to start a conversation with or B to go back: ")
            existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': recipient_name})
            if recipient_name == "B":
                return False
            if existing_name.status_code != 500:
                valid = True

    participants = (username, recipient_name)
    existing_conv = requests.get('http://127.0.0.1:5000/view-messages', json={'participants': participants})

    if existing_conv.status_code != 500 and existing_conv.status_code != 200:
        valid = False
        while not valid:
            recipient_name = input("This conversation already exists, select another user or press B to go back: ")
            conv_participants = (username, recipient_name)
            participants = frozenset(conv_participants)
            existing_conv = requests.get('http://127.0.0.1:5000/view-messages', json={'participants': participants})
            if recipient_name == "B":
                return False
            if existing_conv.status_code == 500:
                valid = True
    message = input("Enter a message to begin the conversation: ")
    message_dict = {
        "content": message,
        "sender": username,
        "timestamp": datetime.datetime.utcnow().strftime('%B %d %Y')
    }

    new_conversation = {
        "participants": participants,
        "starter": participants[0],
        "receiver": participants[1],
        "messages": [message_dict]
    }

    requests.post('http://127.0.0.1:5000/start-new-conversation', json=new_conversation)
    print("Message sent!")


def view_conversations(user):
    username = user.get('username')
    count = 1
    conversation_list = requests.get('http://127.0.0.1:5000/view-conversations', json={'username': username}).json()
    for name in conversation_list:
        print(count, ": ", name)
        count += 1
    print("Select the number of the conversation you want to view")
    selection = WConio2.getkey()
    if 0 <= int(selection) - 1 < len(conversation_list):
        recipient = conversation_list[int(selection) - 1]
        participants = (username, recipient)
        messages = requests.get('http://127.0.0.1:5000/view-messages', json={'participants': participants}).json()
        print(messages)
        print("Would you like to send a message in this conversation? Y/N")
        send_new = WConio2.getkey()
        while send_new != 'Y' and send_new != 'N':
            print("Try again, would you like to send a message in this conversation? Y/N? ")
            send_new = WConio2.getkey()
        if send_new == 'Y':
            send_message(user, recipient)
    else:
        print("Invalid selection, please try again")
        return


def send_message(user, preselected):
    username = user.get('username')
    if preselected is None:
        recipient = input("Enter the username of the recipient of this message: ")
    else:
        recipient = preselected
    existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': recipient})
    if existing_name.status_code == 500:
        valid = False
        while not valid:
            print("Cannot find a user with that user name")
            recipient = input("Enter the username of the person you want to message or B to go back: ")
            existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': recipient})
            if recipient == "B":
                return False
            if existing_name.status_code != 500:
                valid = True
    message_content = input("Enter the message you want to send: ")
    participants = (username, recipient)
    message_dict = {
        "content": message_content,
        "sender": username,
        "timestamp": datetime.datetime.utcnow().strftime('%B %d %Y')
    }
    requests.post('http://127.0.0.1:5000/send-message', json={
        "participants": participants,
        "message": message_dict
    })

    print("Successfully sent message")

