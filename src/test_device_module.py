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
            "registration_date": "July 4 2022"
        }
        improperly_formatted_device = {
            "type": "Heart Rate Monitor",
            "name": "Tony's Nuclear Reactor",
            "username": "Tony",
            "assignee": "Tony",
            "MAC": "7Y745745H",
            "registration_date": "May 4 2022"
        }
        unrecognized_type_device = {
            "type": "Mind control device",
            "name": "Mantis' antenna",
            "user": "Mantis",
            "assignee": "Thanos",
            "MAC": "1D234578",
            "registration_date": "June 6 2021"
        }
        properly_formatted_heart_rate = {
            "device_type": "Heart Rate Monitor",
            "heart_rate": "120",
            "diastolic_bp": "120",
            "systolic_bp": "80",
            "reading_date": "February 15 2022"
        }
        incorrectly_formatted_heart_rate = {
            "device_type": "Heart Rate Monitor",
            "heartbeat": "",
            "reading_date": "February 14 2020"
        }
        invalid_number_heart_rate = {
            "device_type": "Heart Rate Monitor",
            "heart_rate": "-5",
            "diastolic_bp": "120",
            "systolic_bp": "80",
            "reading_date": "February 15 2022"
        }
        properly_formatted_oxygen = {
            "device_type": "Blood Oxygen Monitor",
            "oxygen": "99",
            "reading_date": "February 15 2022"
        }
        incorrectly_formatted_oxygen = {
            "device_type": "Heart Rate Monitor",
            "heartbeat": "",
            "reading_date": ""
        }
        invalid_number_oxygen = {
            "device_type": "Blood Oxygen Monitor",
            "oxygen": "-99",
            "reading_date": "February 15 2022"
        }
        properly_formatted_weight = {
            "device_type": "Scale",
            "weight": "101",
            "reading_date": "February 15 2022"
        }
        incorrectly_formatted_weight = {
            "device_type": "Scale",
            "heartbeat": "",
            "reading_date": ""
        }
        invalid_number_weight = {
            "device_type": "Scale",
            "weight": "-99",
            "reading_date": "February 15 2022"
        }
        properly_formatted_glucose = {
            "device_type": "Glucometer",
            "glucose": "90",
            "reading_date": "February 15 2022"
        }
        incorrectly_formatted_glucose = {
            "device_type": "Glucometer",
            "glue": "",
            "reading_date": ""
        }
        invalid_number_glucose = {
            "device_type": "Glucometer",
            "glucose": "-120",
            "reading_date": "February 15 2022"
        }
        properly_formatted_temperature = {
            "device_type": "Thermometer",
            "temperature": "94",
            "reading_date": "February 15 2022"
        }
        incorrectly_formatted_temperature = {
            "device_type": "Thermometer",
            "temp": "86",
            "reading_date": ""
        }
        invalid_number_temperature = {
            "device_type": "Thermometer",
            "temperature": "-2",
            "reading_date": "February 15 2022"
        }
        incorrect_type_reading = {
            "device_type": "Heart Rate Monitor",
            "glucose": "",
            "reading_date": ""
        }

        self.assertEqual(dev.check_device_type(properly_formatted_device), True)
        self.assertEqual(dev.check_device_type(improperly_formatted_device), True)
        self.assertEqual(dev.check_device_type(unrecognized_type_device), "Unrecognized device type")
        self.assertEqual(dev.check_device_format(properly_formatted_device), True)
        self.assertEqual(dev.check_device_format(improperly_formatted_device), "Incorrect device format")
        self.assertEqual(dev.check_device_format(unrecognized_type_device), True)
        self.assertEqual(dev.check_health_reading_format(properly_formatted_heart_rate), True)
        self.assertEqual(dev.check_health_reading_format(incorrectly_formatted_heart_rate),
                         "Invalid health reading format")
        self.assertEqual(dev.check_health_reading_format(invalid_number_heart_rate), "Invalid integer")
        self.assertEqual(dev.check_health_reading_format(properly_formatted_oxygen), True)
        self.assertEqual(dev.check_health_reading_format(incorrectly_formatted_oxygen),
                         "Invalid health reading format")
        self.assertEqual(dev.check_health_reading_format(invalid_number_oxygen), "Invalid integer")
        self.assertEqual(dev.check_health_reading_format(properly_formatted_weight), True)
        self.assertEqual(dev.check_health_reading_format(incorrectly_formatted_weight),
                         "Invalid health reading format")
        self.assertEqual(dev.check_health_reading_format(invalid_number_weight), "Invalid integer")
        self.assertEqual(dev.check_health_reading_format(properly_formatted_glucose), True)
        self.assertEqual(dev.check_health_reading_format(incorrectly_formatted_glucose),
                         "Invalid health reading format")
        self.assertEqual(dev.check_health_reading_format(invalid_number_glucose), "Invalid integer")
        self.assertEqual(dev.check_health_reading_format(properly_formatted_temperature), True)
        self.assertEqual(dev.check_health_reading_format(incorrectly_formatted_temperature),
                         "Invalid health reading format")
        self.assertEqual(dev.check_health_reading_format(invalid_number_temperature), "Invalid integer")

        self.assertEqual(dev.check_health_reading_format(incorrect_type_reading), "Invalid health reading format")
        self.assertEqual(dev.check_date_format("May 11 2012"), True)
        # self.assertEqual(dev.check_date_format("May 11, 2012"), False)


if __name__ == '__main__':
    unittest.main()
