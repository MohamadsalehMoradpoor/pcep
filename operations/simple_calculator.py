i = input('please inter a number: ')
i = int(i)
j = input('please inter another number: ')
j = int(j)
k = input('please inter a operation (+ , - , * , /): ')
if k == ('+'):
    print(i + j)
elif k == ('-'):
    print(i - j)
elif k == ('*'):
    print(i * j)
elif k == ('/') and j != 0:
    print(i / j)
else:
    print('Not a valid operation or operator')