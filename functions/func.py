def search_customers (x, y=0):
    customers = ['09121234', '09131234', '09131234']
    if x in customers:
        return 10
    else:
        return 20

i = input('please Enter a Phone Number: ')
result = search_customers (i)
if result == 10 :
    print('Yes, The Customer Exists')
elif result == 20 :
    print('No, The Customer Does Not Exists')

result = search_customers ('09151234')