from flask import Flask, jsonify, request
import pymongo
import device_module

app = Flask(__name__)

client = pymongo.MongoClient(
    "mongodb+srv://Github:Github@cluster0.pkk8t.mongodb.net/Test1?retryWrites=true&w=majority")

db = client["Test1"]
devices = db["Devices"]
users = db["Users"]


# @app.route("/test-post", methods=["POST"])
# def setName():
#     if request.method == 'POST':
#         posted_data = request.get_json()
#         data = posted_data['name']
#         print("Successfully stored  " + str(data))
#         return jsonify(str("Successfully stored  " + str(data)))
#
#
# @app.route("/test-get", methods=["GET"])
# def message():
#     posted_data = request.get_json()
#     name = posted_data['name']
#     return jsonify(name)


@app.route("/add-new-user", methods=["POST"])
def add_new_user():
    if request.method == 'POST':
        posted_data = request.get_json()
        user = posted_data['user_info']
        users.insert_one(user)
        return jsonify(str("Successfully added  " + str(user)))


@app.route("/find-user", methods=["GET"])
def find_user():
    target = request.get_json()
    username = target['username']
    existing_name = users.find_one({'username': username})
    existing_name['_id'] = str(existing_name['_id'])
    return existing_name


@app.route("/authenticate", methods=["GET"])
def find():
    target = request.get_json()
    username = target['name']
    password = target['password']
    existing_name = users.find_one(
        {'username': username,
         'password': password})
    existing_name['_id'] = str(existing_name['_id'])
    return existing_name


@app.route("/add-new-device", methods=["POST"])
def add_new_device():
    if request.method == 'POST':
        posted_data = request.get_json()
        device = posted_data['device']
        check = device_module.check_device_format(device)
        if check:
            devices.insert_one(device)
            return jsonify(str("Successfully stored  " + str(device)))
        else:
            return False


@app.route("/find-device", methods=["GET"])
def find_device():
    target = request.get_json()
    existing_name = devices.find_one(target)
    existing_name['_id'] = str(existing_name['_id'])
    return existing_name


@app.route("/view-devices", methods=["GET"])
def view():
    target = request.get_json()
    devices_list = []
    for device in devices.find({"user": target['name']}, {"_id": 0, "name": 1}):
        devices_list.append(device['name'])
    return jsonify(devices_list)


@app.route("/new-reading", methods=["POST"])
def create_reading():
    target = request.get_json()
    username = target['name']
    reading = target['health_reading']
    users.update_one(
        {'username': username},
        {'$push': {'health_records': reading}})
    return jsonify(str("Successfully stored  " + str(reading)))


if __name__ == '__main__':
    app.run(debug=True)
