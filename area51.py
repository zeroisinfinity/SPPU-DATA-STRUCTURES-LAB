s = ''
for i in range(300):
    if i < 150:
        s += '([{'
    else:
        s+="}])"


def fact(n):
    return n*(lambda x : fact(x - 1) if x>1 else 1)(n)
n = 6
fact = (lambda x : x*fact(x - 1) if x>1 else 1)
print(fact(n))
