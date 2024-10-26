arrayList = list(range(1, 101))

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

output = []
for val in reversed(arrayList):
    if isPrime(val):
        continue
    elif val % 3 == 0 and val % 5 == 0:
        output.append("FooBar")
    elif val % 3 == 0:
        output.append("Foo")
    elif val % 5 == 0:
        output.append("Bar")
    else:
        output.append(str(val))

print(' '.join(output))