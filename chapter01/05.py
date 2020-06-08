def n_gram(target, n):
    return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]


target = "I am an NLPer"
# 文字
print(n_gram(target, 1))

words = target.split(' ')
# 単語
print(n_gram(words, 1))
