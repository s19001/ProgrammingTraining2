x_str = "paraparaparadise"
y_str = "paragraph"


def n_gram(sentence, N):
    result = []
    for it in range(len(sentence)):
        if it + N > len(sentence):
            return result
        result.append(sentence[it: it+N])


X = set(n_gram(x_str, N=2))
Y = set(n_gram(y_str, N=2))

print(X)
print(Y)


_sum = X | Y

print(_sum)

_intersection = X & Y

print(_intersection)

_diff_X = X - Y
_diff_Y = Y - X

print(_diff_X)
print(_diff_Y)

# `se`を含むか
print('se' in X)

print('se' in Y)
