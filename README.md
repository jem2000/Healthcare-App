# Healthcare-App

## Branching structure
### Building the core application will be done in the main branch. This includes functionalities such as the basic shell prompt as well as an authentication system. In order to implement the different use cases, a new branch will be used. This will allow me to easily identify if adding one feature breaks another one. Branches will be closed using pull requests when features are fully implemented to ensure cleanliness of the repo. 

### Note: I initially built a command-line interface for this application. However, since the goal of this project is to build an API backend, I will be building this using a flask server, and using the CLI as a way to ensure that I have included all the necessary functionalities in my APIs. 

### My APIs

#### http://127.0.0.1:5000/add-new-user -> Create a new user
Ex. requests.post('http://127.0.0.1:5000/add-new-user', json={'user_info': user_info})

#### http://127.0.0.1:5000/find-user -> Check if a username exists 
Ex. existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': username})

#### http://127.0.0.1:5000/authenticate -> Check if a username and password combination exists
Ex. existing_account = requests.get('http://127.0.0.1:5000/authenticate', json={
        'name': username,
        'password': password
    })
        
#### http://127.0.0.1:5000/add-new-device -> Add a new device
Ex. requests.post('http://127.0.0.1:5000/add-new-device', json=new_device)

#### http://127.0.0.1:5000/find-device -> Check if a device name exists
Ex. existing_name = requests.get('http://127.0.0.1:5000/find-device', json={'name': device_name})  
Ex 2. existing_MAC = requests.get('http://127.0.0.1:5000/find-device', json={'MAC': device_MAC})

#### http://127.0.0.1:5000/view-devices -> View all the devices under a registered user
Ex. device_list = requests.get('http://127.0.0.1:5000/view-devices', json={'name': username}).json()

#### http://127.0.0.1:5000/new-reading -> Add a new health reading to the current user
Ex. requests.post('http://127.0.0.1:5000/new-reading', json={
        'name': username,
        'health_reading': health_reading
    })
    
    
Things to do:  
1. Add data checking, not only structure checking  
2. Implements class structure in modules  
