
def patron(x):

    for i in range(x, 0, -1):
        print(' ' * (x - i) + '* ' * i)

    for i in range(2, x + 1):
        print(' ' * (x - i) + '* ' * i)

patron(6)
 






