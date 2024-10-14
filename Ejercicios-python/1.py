print("Normal Pyramid")

for i in range(5):
    x = '*'
    x = x * i
    print(f'{x: ^10}')

print("\nInvert Pyramid")

for i in range(5):
    x = '*'
    x = x * (5 - i)
    print(f'{x: ^10}')  

print("\nLeft sided Pyramid")

for i in range(5):
    x = '*'
    x = x * i
    print(f'{x: <10}')  
print("\nRight sided Pyramid")

for i in range(5):
    x = '*'
    x = x * 1
    print(f'{x: >10}')  


print("  *  ")
print(" * * ")

lista = ["     *     ","    * *    ","   * * *   ","  * * * *  "," * * * * * "]

for i in lista:
    print(i)