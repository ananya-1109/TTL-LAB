#wap to find out the distinct prime factors of a number entered through keyboard
import math
a = int(input("Enter a number"))
if(a%2==0):
    print(2)
    a=a/2
while (a%2==0):
    a=a/2
x=3
while x<=(a/2):
    while (a%x==0):
        print(x)
        a = a/x
    x = x+2
