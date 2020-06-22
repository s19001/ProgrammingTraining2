import re


def cipher(src):
    return re.sub(r'[a-z]', lambda m: chr(219 - ord(m.group(0))), src)


text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might\
 Also Sign Peace Security Clause. Arthur King Can."


print(cipher(text))
print(cipher(cipher(text)))
