import unittest
import device_module as dev


class MyTestCase(unittest.TestCase):
    def test_something(self):
        properly_formatted_device = {
            "type": "Blood Oxygen Monitor",
            "name": "Zemo's Oxygen Monitor",
            "user": "Bucky",
            "assignee": "Mr Doctor",
            "MAC": "5F654363KJ87",
            "registration_date": "today"
        }
        improperly_formatted_device = {
            "type": "Heart Rate Monitor",
            "name": "Tony's Nuclear Reactor",
            "username": "Tony",
            "assignee": "Tony",
            "MAC": "7Y745745H",
            "registration_date": "tomorrow"
        }
        unrecognized_type_device = {
            "type": "Mind control device",
            "name": "Mantis' antenna",
            "user": "Mantis",
            "assignee": "Thanos",
            "MAC": "1D234578",
            "registration_date": "yesterday"
        }
        properly_formatted_reading = {
            "device_type": "Scale",
            "weight": "172",
            "reading_date": "today"
        }
        incorrectly_formatted_reading = {
            "device_type": "Heart Rate Monitor",
            "heartbeat": "",
            "reading_date": ""
        }
        incorrect_type_reading = {
            "device_type": "Heart Rate Monitor",
            "glucose": "",
            "reading_date": ""
        }

        self.assertEqual(dev.check_device_type(properly_formatted_device), True)
        self.assertEqual(dev.check_device_type(improperly_formatted_device), True)
        self.assertEqual(dev.check_device_type(unrecognized_type_device), False)
        self.assertEqual(dev.check_device_format(properly_formatted_device), True)
        self.assertEqual(dev.check_device_format(improperly_formatted_device), False)
        self.assertEqual(dev.check_device_format(unrecognized_type_device), True)
        self.assertEqual(dev.check_health_reading_format(properly_formatted_reading), True)
        self.assertEqual(dev.check_health_reading_format(incorrectly_formatted_reading), False)
        self.assertEqual(dev.check_health_reading_format(incorrect_type_reading), False)


if __name__ == '__main__':
    unittest.main()
