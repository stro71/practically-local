import string
from random import *

def ran_gen(num_len=8):
    characters = string.ascii_letters + string.punctuation  + string.digits
    return "".join(choice(characters) for x in range(num_len))

print ("Here is your random password: ")

print(ran_gen())
print(ran_gen(15))
print (ran_gen(30))