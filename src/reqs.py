import requests
import datetime

health_reading = {
    "device_used": "device 1",
    "blood_pressure": "120/80",
    "heart_rate": "90",
    "oxygen": "99",
    "glucose": "90",
    "weight": "150",
    "height": "5'9",
    "reading_date": datetime.datetime.utcnow().strftime('%B %d %Y')
}

test_device = {
    "type": "pacemaker",
    "name": "Zero's pacemaker",
    "user": "Patient Zero",
    "assignee": "Mr Doctor",
    "MAC": '5F8538295',
    "registration_date": datetime.datetime.utcnow().strftime('%B %d %Y')
}

if __name__ == '__main__':
    myDict = {"name": health_reading}
    # res = requests.post('http://127.0.0.1:5000/test-post', json=myDict)
    # dictFromServer = res.json()

    # res = requests.get('http://127.0.0.1:5000/test-get', json=myDict)
    # print(res.json())

    # new_device = {'device': test_device}
    # res = requests.post('http://127.0.0.1:5000/add-new-device', json=new_device)

    res = requests.get('http://127.0.0.1:5000/find-device', json={'name': 'Zero\'s Heart Monitor'})
