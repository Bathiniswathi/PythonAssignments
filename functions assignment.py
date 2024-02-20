
#write a function which contains some numbers as args  and printsquare of that no

def square(x):
    return x ** 2

number = int(input("Enter  a number:"))
print("square of",number,"is:",square(number))


#write a function given number is even or odd

num = int(input("enter a number:"))#input an integer


def Even_or_odd(num):
    if num == 0:
        print(num,"is neither odd nor even")
    elif num % 2 == 0:
        print(num,"is an even number")
    else:
        print(num,"is an odd number")

Even_or_odd(num)#function call  



#write a function to find factorial of given numbers

def factorial(m):
    fact = 1
    for i in range(1,m+1):
        fact = fact*i
        print("factorial of ",m,"is",fact)
        n = int(input("enter a number:"))
        factorial(n)




#write a program using function  for addition,sub,mul,division
        

def calculation(x,y):
    addition = x+y
    subtraction = x-y
    return addition,subtraction
c,d = calculation(20,10)
print("addition and subtraction of number is: ",c,d)



#multiplication

def mul_num(a,b):
    mul = a*b
    return mul

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

print("multiplication of two numbers is: " ,mul_num(num1,num2))


#divison
def division(*args):
    sum = 1
    for i in args:
        sum /= i
        return sum
    print(int(divison(400/100/2)))               

