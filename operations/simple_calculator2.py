i = input('please inter a number: ')
i = int(i)
j = input('please inter another number: ')
j = int(j)
k = input('please inter a operation (+ , - , * , /): ')
valid_operations = ['+', '-', '*', '/']
if k in valid_operations:
    print('valid operation')
else:
    print('Not a valid operation or operator')