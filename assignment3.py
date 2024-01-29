#1.calculate the sum of all numbers from 1 to a given number.
num = int(input("enter the number:"))
sum = 0
for i in range(1,num+1):
    sum = sum+i
    i=i+1
print("sum=",sum)

#2.write a program to print multiplication table of a given number.
num = int(input("enter the table:"))
for i in range(1,11):
    print(num,'x',i'=',num*i)


#3.display numbers  from a list using loop.

list = [10,20,,30,40,50,60]
for num in list:
    print(sum)

#count the total number of digits in a number
num =input("enter the number:")
print(len(num))


#5.print list in reverse order using a loop.
n=int(input("enter a number:"))
while n >0:
    r=n%10
    print(r)
    n=n//10


#display numbers from -10 to -1 using for loop.
for i in range(-10,0):
      print(i)        

#7.use else block to display a message "Done"after execution of for loop.           

for i in range(1,101):
    print(i)
else:
    print("Done")

#8.write a program to display all prime numbers in range
    
num=int(input("enter the number to print prime numbers with in the range:"))
for i in range(num + 1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
            else:
                print(i)


#reverse  a given integer number.
num=int(input("enter the number:"))
reversedNum=num[::-1]
print(reversedNum)

#write a program to display all prime numbers within range

low=int(input("enter the  first number:"))
hig=int(input("enter the second number:"))
for num in range(low,hig+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)


#11.reverse a given integer number

for i in range(10,0,-1):
    print(i,end=' , ')

#12.use loop to display elements from a given listpresent at odd index positions                                    

list=[2,1,42,57,52,34,9,3]
for i in list:
    if(i%2==0):

        print(i,"is odd")
    else:
        print(i,"is even")

#13.calculate the cube of all num from 1 to a given number


a=4
cube=a*a*a
print("the cube of that number is",cube)


#find the sum of the sereies upto n terms
sum = 0
i =0 
print(end="enter the value of n:")
n=int(input())
print(end="enter" + str(n) + "numbers:")
while i<n:
    num = int(input())
    sum = sum+num
    i = i+1
    print("\nsum of "+str(n) + "numbers = "+str(sum))



   




