#2.Write a python program to input 3 numbers as a,b,c then display 1 if those are sides of a triangle otherwise display 0.
a=int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(input("enter side 3:"))

if a+b>c and b+c>a and a+c>b:
    print("1")
else:
    print("0")

#wap to input a 3 numbers as a,b,c then display one if those are sides of a triangle otherwise display 0
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
if (a+b)>c and (c+a)>b and (b+c)>a:
    print(1)
else:
    print(0)
