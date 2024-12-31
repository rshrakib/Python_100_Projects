import random
import string


word_len = 18
components = [string.ascii_letters, string.digits,"!@#$%^&*"]

chars = []
for clist in components:
    for item in clist:
        chars.append(item)


def gen_pass():
    password = []
    for i in range(word_len):
        rchar = random.choice(chars)
        password.append(rchar)

    return "".join(password)

print(gen_pass())