#opretors
#arihmetic opretors
#comarision opretors
#logical opretors

#arithmetic opretors
#1.addition(+)
#2.multiplication(*)
#3.subtraction(-)
#divison
#modules(/)


#addition
x=5
y=3
z=x+y
print(z)


#subtraction
x=10
y=5
z=x-y
print(z)

#multiplication
x=5
y=2
z=x*y
print(z)

#divison
x=6
y=2
z=(x/y)
print(z)

#comarision opretor(<,>,==,>=,<=)


a=9
b=4
print("The output of 9 is greater than 4:",a>b)
print("The output of 9 is less than 9:",a<b)
print("The output of 9<=4 is:",a<=b)
print("The output of 9>=4 is:",a>=b)
print("The output of 9 equal to 4 is:",a==b)
print("The output of 9 not equal to 4 is:",a!=b)


#logical opretor
#And
#Or
#not

#And opretor
#oprend1(x)        oprend2(y)     result(x and y)   
#False              False          False
#False              True           False
#True               False          False
#True               True           True 



A=True
B=False
print(A and B)

A=True
B=False
print(A and B)

A=False
B=False
print(A and B)

A=True
B=True
print(A and B)


a=5
print(a > 3 and a < 10)
#returns True because 5 is greater than 3
#AND 5 is less than 10.



#Or opretor
#oprend1(x)     oprend2(y)     result(x,y)
#False           True          True
#True            False         True
#True            True          True
#False           False         False      

x=True
y=False
print(x or y)

x=False
y=True
print(x or y)

x=True
y=True
print(x or y)

x=False
y=False
print(x or y)

x = 5
print(x > 3 or x < 4)
#True because one of the conditions are True 
#(5 is greater than 3,5 is not less than 4)


#not opretor
#x         notx
#False      True
#True        False

x = 5
print(not(x > 3 and x < 10))






