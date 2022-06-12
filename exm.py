#print("hi")
import math
x = input("x=")
print("check", x.isnumeric() == True)
while(x.isnumeric() == False):
    print("false")
    x = input("x=")
if (x.isnumeric()):
    print('number', math.sin(int(x)))
else:
    print("number no no no no")
print("__x___",x)
x = int(x)
if (x <= -7):
    y = x**2
elif (x >= 7):
    y = math.tan(x)
else:
    y = x
print("Answer is", y)
    
