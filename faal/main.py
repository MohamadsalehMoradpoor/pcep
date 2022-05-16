import os
__DIR__ = os.path.dirname(os.path.abspath(__file__))
i = input('Please Inter Birth Month (1-12): ')
if int(i) < 1 or int(i) > 12:
    print('Your Number is not a Valid Month')
else:
    f = open(__DIR__ + '/matneh_falha/' + str(i) + '.txt', 'r')
    m = f.read()

    f = open('faal/natayej.txt', 'w')
    f.write(m)
    f.close()