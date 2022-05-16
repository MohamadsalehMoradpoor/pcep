class calculator:
    def sum (self, x, y):
        return x + y
    def minus (self, x, y):
        return x - y
    def times (self, x, y):
        return x * y
    def division (self, x, y):
        if y==0: 
            return "You can not divide by zero!" 
        else: 
            return x/y
    
Calculation = calculator()
sum1 = Calculation.sum(7, 5)
print (sum1)
Calculation = calculator()
minus1 = Calculation.minus(7, 5)
print(minus1)
Calculation = calculator()
division1 = Calculation.division(7, 5)
print(division1)
Calculation = calculator()
times1 = Calculation.times(7, 5)
print(times1)
print('Done')