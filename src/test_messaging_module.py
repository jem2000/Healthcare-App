import unittest
import messaging_module as msg


class MyTestCase(unittest.TestCase):
    def test_something(self):
        participants = ("a", "b")
        participants2 = ("b", "a")
        participants3 = ("2", "1")
        properly_formatted_conversation = {
            "participants": participants,
            "starter": "me",
            "receiver": "other guy",
            "messages": [{"content": "hi", "sender": "me", "timestamp": "July 4th"}]
        }
        improperly_formatted_conversation = {
            "participants": participants,
            "sender": "me",
            "recipient": "other guy",
            "message_list": [{"content": "hi", "sender": "me", "timestamp": "July 4th"}]
        }
        message_dict = {
            "content": "Hello",
            "sender": "Patient Zero",
            "timestamp": "5/7/21"
        }
        properly_formatted_message = {
            "participants": participants,
            "message": message_dict
        }
        improperly_formatted_message = {
            "message": message_dict
        }
        self.assertEqual(msg.check_conversation_format(properly_formatted_conversation), True)
        self.assertEqual(msg.check_conversation_format(improperly_formatted_conversation),
                         "Incorrect conversation format")
        self.assertEqual(msg.check_message_format(properly_formatted_message), True)
        self.assertEqual(msg.check_message_format(improperly_formatted_message), "Incorrect message format")
        self.assertEqual(msg.alphabetize(participants[0], participants[1]), ("a", "b"))
        self.assertEqual(msg.alphabetize(participants2[0], participants2[1]), ("a", "b"))
        self.assertEqual(msg.alphabetize(participants3[0], participants3[1]), ("1", "2"))


if __name__ == '__main__':
    unittest.main()
