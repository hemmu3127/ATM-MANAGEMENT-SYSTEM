import pickle

# Open the pickle file in read-binary mode
with open('my_pickle.pkl', 'rb') as f:
    accounts = pickle.load(f)

# Now `accounts` will contain the unpickled data (could be a dictionary, list, or any other object)
print(accounts)  # To view the contents of the unpickled data

# Assuming `accounts` is a dictionary, you can access username and password like this:
username = accounts.get('username')  # Replace 'username' with the actual key if different
password = accounts.get('password')  # Replace 'password' with the actual key if different

print("Username:", username)
print("Password:", password)
