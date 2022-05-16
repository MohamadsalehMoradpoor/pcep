class student:
    name = 'saleh'
    def score (self, x , y, z):
        s = (x + y + z)/3
        return s
myStudent = student()
myStudent.name = 'mobina'
result = myStudent.name
print(result)
myStudent2 = student()
result2 = myStudent2.score (12, 18, 20)
print (result2)