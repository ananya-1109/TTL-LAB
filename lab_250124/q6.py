### wap to input a decimal number then convert it into equivalent numbers as follows using switch case statement 
#binary number, octal number, hexadecimal number
a = int(input("Enter a number"))
print("SELECT THE FOLLOWING OPTION")
print("Press - 1 for Decimal to Binary")
print("Press - 2 for Decimal to Octal")
print("Press - 3 for Decimal to Hexadecimal")
p = input("Choose")

match p:
    case "1":
        print(bin(a))
    case "2":
        print(oct(a))
    case "3":
        print(hex(a))
    case _:
        print("ERROR")


#6.Write a python program to input a decimal number then convert it into equivalent number as follows using switch case statement.
#1st ) Binary NUMBER 
#2nd ) Octal NUMBER
#3rd) Hexadecimal NUMBER
num=(input("enter a decimal number:"))
a=(input("enter the conversion you want:"))
match a:
        case "binary":
            print(bin(num))
        case "octal":
            print(oct(num))
        case "hexadecimal":
            print(hex(num))
