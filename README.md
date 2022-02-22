# Healthcare-App

## Branching structure
### Building the core application will be done in the main branch. This includes functionalities such as the basic shell prompt as well as an authentication system. In order to implement the different use cases, a new branch will be used. This will allow me to easily identify if adding one feature breaks another one. Branches will be closed using pull requests when features are fully implemented to ensure cleanliness of the repo. 

### Note: I initially built a command-line interface for this application. However, since the goal of this project is to build an API backend, I will be building this using a flask server, and using the CLI as a way to ensure that I have included all the necessary functionalities in my APIs. 

### My APIs

#### http://127.0.0.1:5000/find-user -> Check if a username exists 
##### Ex. existing_name = requests.get('http://127.0.0.1:5000/find-user', json={'username': username})
