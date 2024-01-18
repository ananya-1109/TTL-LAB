#1.assign different types of values to different variables, print them and display all the variables which you have created.
#Then display the types of all variables and delete a particular variable.

x=5000
print(x)

y="string"
del y
#print(y)

z=9.56
print(z)

p='true'
print(p)

#del(p)

print(type(x))
#print(type(y))
print(type(z))
print(type(p))



#2.write a python program to input a 4-digit integer number then find and print 1st and last digit of it using only operators.
number=int(input("enter a 4 digit number:"))
first_digit=number/1000
print(int(first_digit))
last_digit=number%10
print(last_digit)



#3.write a python program to input your first name and last name and then combine both of thr name and print it,where the last name followed by firs
x=str(input("enter your first name: "))
y=str(input("enter your last name: "))

print(y + " " + x)



#4.assign two variables with integer values then print and compare memory location of two variables
x=1234
y=2345
print(x,y)
a=id(x)
b=id(y)
a==b
a>b



#5.input two integers then perform division operation in floating point and integer format.
x=int(input("enter value1:")) #value1
y=int(input("enter value2:")) #value2

div=x/y #division

print(div) #print



#6.write a python program to swap the contents of two variables using single statement.
a="xyz"
b="pqr"
print(a+" "+b)
a,b = b,a
print("after swapping a:",a, "b:" ,b)




#7.initialize a set of elements within a variable and check whether a particular element is available within this set or not using operators only.
a=[1,2,3,4,5,6,7,8,9,10]
# x =input("enter the number to be searched:")
print (2 in a)
print (12 in a)



#8.write python program to find out the distance between two coordinates (x1,y1) and (x2,y2) using only operators.
x1=10
x2=2
y1=3
y2=20

distance=(((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))*(1/2))

print("distance is:", distance)

