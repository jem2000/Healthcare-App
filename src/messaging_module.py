participants_tup = ("", "")

message_dict = {
    "content": "",
    "sender": "",
    "timestamp": ""
}

message_wrapper = {
    "participants": participants_tup,
    "message": message_dict
}

conversation_dict = {
    "participants": participants_tup,
    "starter": "",
    "receiver": "",
    "messages": [message_dict]
}


def alphabetize(sender, receiver):
    myList = [sender, receiver]
    myList.sort()
    return tuple(myList)


def check_conversation_format(new_conversation):
    if new_conversation.keys() != conversation_dict.keys():
        return "Incorrect conversation format"
    if len(new_conversation.get('participants')) != 2:
        return "Incorrect participants format"
    for message in new_conversation.get('messages'):
        if message.keys() != message_dict.keys():
            return "Incorrect participants format"
    return True


def check_message_format(new_message):
    if new_message.keys() != message_wrapper.keys():
        return "Incorrect message format"
    else:
        return True

#
# if __name__ == '__main__':
#     tup = ("sender", "receiver")
#     participants = alphabetize(tup[0], tup[1])
#     my_dict = {
#         "participants": participants,
#         "starter": "me",
#         "receiver": "other guy",
#         "messages": [{"content": "hi", "sender": "me", "timestamp": "July 4th"}]
#     }
#     check = check_conversation_format(my_dict)
#     print(check)
