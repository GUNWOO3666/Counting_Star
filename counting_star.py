for i in range(5):
    print('*' * (i+1))
print("\n")

for i in range(5):
    print('*' * (5 - i))
print("\n")

for i in range(5):
    print(' ' * (4 - i) + '*' * (1 + i))
print("\n")

for i in range(5):
    print(' ' * i + '*' * (5 - i))
print("\n")

for i in range(5):
    print(' ' * (4 - i) + '*' * ((i+1)*2-1) + ' ' * (4 - i))
print("\n")

for i in range(5):
    print(' ' * (i) + '*' * (((4-i)+1)*2-1) + ' ' * (i))
print("\n")