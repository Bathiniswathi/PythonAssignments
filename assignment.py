#compound opretor
x=5
x+=1
print(x)

y='apple'
y+='pie'
print(y)

x=6
x-=4
print(x)

a=3
a*=3
print(3)

y=4
y/=2
print(y)

#identity opretor
x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is z)
print(x is y)
print(x==z)


x=[10,20,30]
y=[10,20,30]
z=y
print(x is not y)
print(y is z)
print(y==z)
print(x!=z)

a=["hi","hello"]
b=["hi","hello"]
print(a is b)

#membership opretor
x=[10,20,30,40]
print(50 in x)

x=[10,20,30,40]
print(10 in x)

x=["apple","banana"]
print("apple" in x)
print("kiwi" in x)
print("guva"not in x )

x=[1,2,3]
print(2 in x )
print(5 in x)
print(6 is not x)

a=["swathi","shobhan","jaiansh","ayaansh"]
print("swathi"in a)
print("rishi" in a)
print("sreyansh" is not a)


z=[20,40,60,80,100,256]
print(200 in z)
print(100 in z)
print(256 in z)

#ternary opretor
#x=first value if condition else second opretor
x=20 if 20>60 else 80
print(x)

y=60 if 40>60 else 100
print(y)

z=100 if 80>100 else 200
print(z)

a=3 if 2>3 else 5
print(a)

b=33.9 if 22.45>33.9 else 55.5
print(b)
print(type(b))


#input output statements
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print(type(a))
print(type(b))
print(a+b)

x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
print(type(x))
print(type(y))
print(x+y)

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print(type(a))
print(type(b))
print(a-b)

b=20
a=input("enter the first number:")
result=eval(a)
print(result)

b=30
a=input("enter the first number:")
result=eval(a)
print(result)

#bitwise opretor
#AND opretor
#sets each bit to 1 if both bits are 1
a=6
a&=3      #6=110
print(a)#3=011->2

x=3
x&=2       #011  
print(x)   #010->010

z=5     #101
z&=3     #011->001
print(z)

b=8  #1000
b&=5 #0101->0000 
print(b)

y=32  #100000
y&=16 #010000->000000
print(y)
#OR opretor
#sets each bit to 1 if one of twobits is 1
x=6   #110
x|=3  #011->111 #0/p =7
print(x)

x=7#111
x|=3#011->#o/p=7
print(x)

x=8#10000
x|=2#00010->#o/p=18
print(x)

a=3#011
a|=3#011->011 o/p is 3
print(a)

z=4#100
z|=3#011=111->7
print(z)

#XOR opretor
#sets each bits to 1 if only one of two bits is 1

print(6 ^ 3)#110
            #011=101->2

print(8 ^ 2)#10000
            #00001=00000->10001=17

print(4 ^ 3) #100
             #011=111=7

#NOT opretor
#inverts the all bits
#0 becomes 1,1 becomes 0

print(~3)



    































