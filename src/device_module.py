device_types = ["Heart Rate Monitor", "Blood Oxygen Monitor", "Scale", "Glucometer", "Thermometer"]

heart_rate_dict = {
    "device_used": "",
    "heart_rate": "",
    "blood_pressure": "",
    "reading_date": ""
}
blood_oxygen_dict = {
    "device_type": "",
    "oxygen": "",
    "reading_date": ""
}
scale_dict = {
    "device_type": "",
    "weight": "",
    "reading_date": ""
}
glucometer_dict = {
    "device_type": "",
    "glucose": "",
    "reading_date": ""
}
thermometer_dict = {
    "device_type": "",
    "temperature": "",
    "reading_date": ""
}
health_reading_dict = {
    "Heart Rate Monitor": heart_rate_dict,
    "Blood Oxygen Monitor": blood_oxygen_dict,
    "Scale": scale_dict,
    "Glucometer": glucometer_dict,
    "Thermometer": thermometer_dict,
}

new_device_dict = {
    "type": "",
    "name": "",
    "user": "",
    "assignee": "",
    "MAC": "",
    "registration_date": ""
}


def check_device_type(new_device):
    if new_device["type"] in device_types:
        return True
    else:
        return False


def check_device_format(new_device):
    if new_device.keys() == new_device_dict.keys():
        return True
    else:
        return False


def check_health_reading_format(new_reading):
    if new_reading.keys() == health_reading_dict[new_reading["device_type"]].keys():
        return True
    else:
        return False
