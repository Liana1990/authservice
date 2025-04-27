import random
import string


characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
print(characters)

code = ''.join(random.choices(characters, k=6))
print(code)

