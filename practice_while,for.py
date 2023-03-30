i = 1
while i < 6:
    print('*' * i)
    i += 1
print('-------------')

i = 5
while i >= 1:
    print('*' * i)
    i -= 1
print('-------------')

i = 5
whitespace = 0
while whitespace < 5:
    print(f"{' ' * whitespace}{'*' * i}")
    i -= 1
    whitespace += 1
print('-------------')

whitespace = 4
i = 1
while i < 6:
    print(f"{' ' * whitespace}{'*' * i}")
    i += 1
    whitespace -= 1