import json
jsonfile='mypass.json'
from cryptography.fernet import Fernet

with open(jsonfile) as jf:
    my_dict = json.load(jf)

print("This is my username: " + my_dict['username'])
print("This is my Password: " + my_dict['password'])
mypass= my_dict['password']
print(mypass)

#We are Encrypted your password
message = mypass.encode("utf-8")
print(message)
key = Fernet.generate_key()
print(key)
f = Fernet(key)
print(f)
encrypted = f.encrypt(message)
print(encrypted)

#We are decrypted your password
decrypted = f.decrypt(encrypted)
print(decrypted)
my_new_pass = decrypted.decode("utf-8")
print(my_new_pass)