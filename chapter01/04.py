let = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might\
 Also Sign Peace Security Clause. Arthur King Can."

initials = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = let.split()

element_symbols = {}

for it, word in enumerate(words):
    if it + 1 in initials:
        element_symbols[it+1] = word[0]
    else:
        element_symbols[it+1] = word[:2]

print(element_symbols)
