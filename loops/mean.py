i = 0
sum = 0
count = 0
while i != '':
    i = input('please Inter a Number(Left Blank to Calculate mean): ')
    if i == '':
        continue
    i = int(i)  
    sum = sum + i
    count = count + 1
    
print(sum / count)