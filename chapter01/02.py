let1 = "パトカー"
let2 = "タクシー"
alt = ""

for (str1, str2) in zip(let1, let2):
    alt += (str1 + str2)
print(alt)
