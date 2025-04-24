import random
import string

def password_generator(length: int = 10):
 alp= string.ascii_letters + string.digits + string.punctuation
 password = "".join(random.choice(alp) for i in range(length))
 return password

pass1 = password_generator()
print("Password Generated: "+pass1)
