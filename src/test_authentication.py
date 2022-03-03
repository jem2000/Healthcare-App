# import unittest
# import mock
# import pymongo
# from bson.objectid import ObjectId
#
# from src.console_application import authentication as auth
#
# client = pymongo.MongoClient(
#     "mongodb+srv://Github:Github@cluster0.pkk8t.mongodb.net/Test1?retryWrites=true&w=majority")
#
# db = client["Test1"]
# col = db["Collection1"]
#
# mock_username = mock.Mock()
# mock_username.return_value = "Patient Zero"
# mock_password = mock.Mock()
# mock_password.return_value = "zero"
# mock_input = mock.Mock()
# mock_input.side_effect = [mock_username.return_value, mock_password.return_value]
#
#
# class MyTestCase(unittest.TestCase):
#     def test_successful_login(self):
#         with mock.patch('builtins.input', mock_input):
#             user = auth.login()
#         credentials = {
#             "patient": True,
#             "doctor": False,
#             "admin": False
#         }
#         patient_zero = {
#             "_id": ObjectId("6209ca67bde52d95c44c5fa9"),
#             "username": "Patient Zero",
#             "password": "zero",
#             "credentials": credentials,
#             "account_creation_time": "February 14 2022"
#         }
#         self.assertEqual(user, patient_zero)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()
