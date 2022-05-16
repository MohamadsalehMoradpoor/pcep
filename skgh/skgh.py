game = {
    's':'Sang',
    'k':'Kaghaz',
    'g':'Gheychi'
}
from random import randint

Cumputer_Score = 0
You_Score = 0

while True:
    i = input('Sang(s), Kaghaz(k), Gheychi(g): ')
    if i not in ['s', 'k', 'g']:
        print('Not a Valid Input!')
    print('You Choose: ' + game[i])
    choices = ['s', 'k', 'g']
    random_number = randint(0, 2)
    c = choices [random_number]
    print('Cumputer Choose: ' + game[c])

    if i == c:
        print('Mosaavi Shod!')
    elif i == 's':
        if c == 'k':
            print('Cumputer Wins!')
            Cumputer_Score += 1
        elif c == 'g':
            print('You Win!')
            You_Score += 1
    elif i == 'k':
        if c == 'g':
            print('Cumputer Wins!')
            Cumputer_Score += 1
        elif c == 's':
            print('You Win!')
            You_Score += 1
    elif i == 'g':
        if c == 's':
            print('Cumputer Wins!')
            Cumputer_Score += 1
        elif c == 'k':
            print('You Win!')
            You_Score += 1
    print('........................')
    print('Cumputer Total Score :' + str(Cumputer_Score))
    print('Your Total Score :' + str(You_Score))
    print('........................')
    t = input('Continue? (y/n): ')
    if t == 'y':
        pass
    elif t == 'n':
        break