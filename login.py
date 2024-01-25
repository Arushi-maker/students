# login.py

# Define a dictionary to store valid usernames and passwords
user_credentials = {
    'Arushi': 'donteven',
    'Ananya': 'ducks',
    # Add more users as needed
}

def login():
    # Prompt the user for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the provided credentials are valid
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful! Welcome, {}.".format(username))
        # Add code for the actions to be performed after successful login
    else:
        print("Invalid username or password. Please try again.")

# Call the login function
login()
