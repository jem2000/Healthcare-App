import unittest
import auth_module as auth

correct_name_dict = {
    "name": "Justin"
}
incorrect_key_name_dict = {
    "user": "Justin"
}
incorrect_type_name_dict = {
    "name": 12
}
correct_creds_dict = {
    "patient": True,
    "doctor": False,
    "admin": False
}
incorrect_key_creds_dict = {
    "patient": True,
    "doctor": False,
}
incorrect_type_creds_dict = {
    "patient": "True",
    "doctor": "False",
    "admin": "False"
}
correct_new_user_dict = {
    "username": "Justin",
    "password": "password",
    "credentials": correct_creds_dict,
    "health_records": [],
    "account_creation_time": "December 12 2021"
}
incorrect_key_new_user_dict = {
    "user": "Justin",
    "pw": "password",
    "creds": correct_creds_dict,
    "health_records": [],
    "account_creation_time": "December 12 2021"
}
incorrect_creds_user_dict = {
    "username": "Justin",
    "password": "password",
    "credentials": incorrect_type_creds_dict,
    "health_records": [],
    "account_creation_time": "December 12 2021"
}
incorrect_password_new_user_dict = {
    "username": "Justin",
    "password": 123,
    "credentials": correct_creds_dict,
    "health_records": [],
    "account_creation_time": "December 12 2021"
}


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(auth.check_find_username(correct_name_dict), True)
        self.assertEqual(auth.check_find_username(incorrect_key_name_dict), "Incorrect name format")
        self.assertEqual(auth.check_find_username(incorrect_type_name_dict), "Name must be a string")
        self.assertEqual(auth.check_credentials(correct_creds_dict), True)
        self.assertEqual(auth.check_credentials(incorrect_key_creds_dict), "Credential keys unrecognized")
        self.assertEqual(auth.check_credentials(incorrect_type_creds_dict), "Credentials must be of type bool")
        self.assertEqual(auth.check_new_user(correct_new_user_dict), True)
        self.assertEqual(auth.check_new_user(incorrect_key_new_user_dict), "Incorrect user format")
        self.assertEqual(auth.check_new_user(incorrect_creds_user_dict), "Invalid user credentials")
        self.assertEqual(auth.check_new_user(incorrect_password_new_user_dict), "Username and password must be strings")


if __name__ == '__main__':
    unittest.main()
