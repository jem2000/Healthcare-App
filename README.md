# Healthcare-App

## Branching structure
### Building the core application will be done in the main branch. This includes functionalities such as the basic shell prompt as well as an authentication system. In order to implement the different use cases, a new branch will be used. This will allow me to easily identify if adding one feature breaks another one. Branches will be closed using pull requests when features are fully implemented to ensure cleanliness of the repo. 

### Note: I initially built a command-line interface for this application. However, since the goal of this project is to build an API backend, I will be building this using a flask server, and using the CLI as a way to ensure that I have included all the necessary functionalities in my APIs. 

### My EC2 Server

http://54.145.228.230

Note: This has been taken down due to the AWS free tier limits.

## My APIs

### Authentication Module

#### http://54.145.228.230/add-new-user -> Create a new user
Ex. requests.post('http://54.145.228.230/add-new-user', json={'user_info': user_info})

#### http://54.145.228.230/find-user -> Check if a username exists 
Ex. existing_name = requests.get('http://54.145.228.230/find-user', json={'username': username})

#### http://54.145.228.230/authenticate -> Check if a username and password combination exists
Ex. existing_account = requests.get('http://54.145.228.230/authenticate', json={  
        &nbsp; 'name': username,  
        &nbsp; 'password': password  
    })
    
### Device Module
        
#### http://54.145.228.230/add-new-device -> Add a new device
Ex. requests.post('http://127.0.0.1:5000/add-new-device', json=new_device)

#### http://54.145.228.230/find-device -> Check if a device name exists
Ex. existing_name = requests.get('http://54.145.228.230/find-device', json={'name': device_name})  
Ex 2. existing_MAC = requests.get('http://54.145.228.230/find-device', json={'MAC': device_MAC})

#### http://54.145.228.230/view-devices -> View all the devices under a registered user
Ex. device_list = requests.get('http://54.145.228.230/view-devices', json={'name': username}).json()

#### http://54.145.228.230/new-reading -> Add a new health reading to the current user
Ex. requests.post('http://54.145.228.230/new-reading', json={  
        &nbsp; 'name': username,  
        &nbsp; 'health_reading': health_reading  
    })
    
### Messaging Module

#### http://54.145.228.230/start-new-conversation -> Starts a new conversation with a user you have never messaged before
Ex. requests.post('http://54.145.228.230/start-new-conversation', json=new_conversation = {  
        &nbsp; "participants": participants,  
        &nbsp; "starter": participants[0],  
        &nbsp; "receiver": participants[1],  
        &nbsp; "messages": [message_dict]  
    })  
Note: sample_message_dict = {  
        &nbsp; "content": message_content,  
        &nbsp; "sender": username,  
        &nbsp; "timestamp": datetime.datetime.utcnow().strftime('%B %d %Y')  
    }
    
#### http://54.145.228.230/view-conversations -> Returns a list of all the people you have conversations with
Ex. conversation_list = requests.get('http://54.145.228.230/view-conversations', json={'username': username}).json()

#### http://54.145.228.230/view-messages -> Returns a list of all the messages that have been sent to or received from a particular user
Ex. messages = requests.get('http://54.145.228.230/view-messages', json={'participants': (username, recipient)}).json()

#### http://54.145.228.230/send-message
Ex. requests.post('http://54.145.228.230/send-message', json={  
        &nbsp; "participants": participants,  
        &nbsp; "message": message_dict  
    })
    
    
Things to do:  
1. Add data checking, not only structure checking  
2. Implements class structure in modules  
