#3.Write a python program to read an alphabet from the user and convert it into opposite case.(If lower then upper, if upper then lower)
str=input("enter an alphabet:")
x=str.swapcase()
print(x)

#wap to read an alphabet from the user and convert it into opposite case
a = input("Enter an alphabet")
if a.islower():
    a=a.upper()
else:
    a=a.lower()
print(a)
