#1.Write a python program to input a 3 digit number and check whether it is palindrome number or not without using loop.
num=(input("enter a 3 digit number:"))
if num==num[::-1]:
    print("number is palindrome")
else:
    print("number is not palindrome")



#wap to input a 3 digit number and check weather it is palindrome number or not without using loop
a = int(input("Enter a 3 digit number"))
k = int(a%10)
i = int(a/100)
temp = (a%100)
j = int(temp/10)
if i==k:
    print("Palindrome")
else:
    print("Not Palindrome")
