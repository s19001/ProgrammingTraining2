import re
sentense = "Now I need a drink, alcoholic of course, after the heavy lectures\
 involving quantum mechanics."
splited = re.split('\s', sentense.replace('.', ''))
splited_len = list(map(len, splited))

print(splited_len)

# for i in range(0, len(splited)):
#     cntlist.insert(i, len(splited[i]))
