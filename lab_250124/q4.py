#4.Write a python program to generate Fibonacci series upto specified number of terms.
n=int(input("enter the length of fibonaaci:"))
a=0
b=1
if n<=0:
    print("the output is:",a, end=" ")
else:
    for x in range(1,n):
        c=a+b
        print(c, end=" ")
        a=b
        b=c


#wap to generate fibonacci series upto specified number of terms
i=int(input("Enter limit"))
t1 = 0
t2 = 1
p = t1+t2
print(t1 , t2, end=" ")

for x in range(3,(i+1)):
    print(p, end=" ")
    t1 = t2;
    t2 = p
    p = t1 + t2
