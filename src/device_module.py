import datetime

device_types = ["Heart Rate Monitor", "Blood Oxygen Monitor", "Scale", "Glucometer", "Thermometer"]

heart_rate_dict = {
    "device_type": "",
    "heart_rate": "",
    "diastolic_bp": "",
    "systolic_bp": "",
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
        return "Unrecognized device type"


def check_device_format(new_device):
    if new_device.keys() == new_device_dict.keys():
        return True
    else:
        return "Incorrect device format"


def check_health_reading_format(new_reading):
    if new_reading.keys() == health_reading_dict[new_reading["device_type"]].keys():
        if new_reading["device_type"] == device_types[0]:
            if check_heart_rate(new_reading) is not True:
                return "Invalid integer"
        elif new_reading["device_type"] == device_types[1]:
            if check_oxygen(new_reading) is not True:
                return "Invalid integer"
        elif new_reading["device_type"] == device_types[2]:
            if check_weight(new_reading) is not True:
                return "Invalid integer"
        elif new_reading["device_type"] == device_types[3]:
            if check_glucose(new_reading) is not True:
                return "Invalid integer"
        elif new_reading["device_type"] == device_types[4]:
            if check_temperature(new_reading) is not True:
                return "Invalid integer"
        return True
    else:
        return "Invalid health reading format"


def check_heart_rate(new_reading):
    if new_reading["device_type"] != device_types[0]:
        return False
    try:
        diastolic = int(new_reading["diastolic_bp"])
        systolic = int(new_reading["systolic_bp"])
        hr = int(new_reading["heart_rate"])
        if diastolic < 0 or systolic < 0 or hr < 0:
            return "Invalid integer"
    except ValueError:
        print("Not an integer")
    check_date_format(new_reading["reading_date"])
    return True


def check_oxygen(new_reading):
    if new_reading["device_type"] != device_types[1]:
        return False
    try:
        oxygen = int(new_reading["oxygen"])
        if oxygen < 0:
            return "Invalid integer"
    except ValueError:
        print("Not an integer")
    check_date_format(new_reading["reading_date"])
    return True


def check_weight(new_reading):
    if new_reading["device_type"] != device_types[2]:
        return False
    try:
        weight = int(new_reading["weight"])
        if weight < 0:
            return "Invalid integer"
    except ValueError:
        print("Not an integer")
    check_date_format(new_reading["reading_date"])
    return True


def check_glucose(new_reading):
    if new_reading["device_type"] != device_types[3]:
        return False
    try:
        glucose = int(new_reading["glucose"])
        if glucose < 0:
            return "Invalid integer"
    except ValueError:
        print("Not an integer")
    check_date_format(new_reading["reading_date"])
    return True


def check_temperature(new_reading):
    if new_reading["device_type"] != device_types[4]:
        return False
    try:
        temperature = int(new_reading["temperature"])
        if temperature < 0:
            return "Invalid integer"
    except ValueError:
        print("Not an integer")
    check_date_format(new_reading["reading_date"])
    return True


def check_date_format(date):
    try:
        datetime.datetime.strptime(date, '%B %d %Y')
        return True
    except ValueError:
        raise ValueError("Incorrect date format")
