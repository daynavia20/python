a = 0
b = 1

for i in range(51):
    print(a)
    fibonacci = a+b
    a = b
    b = fibonacci

print(fibonacci)

