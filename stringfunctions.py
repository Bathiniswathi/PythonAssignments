#string:
#collection of characters
#lower()
#upper()
#ends with()
#starts with()
#replace()
#split()
#count()
#Rstrip()
#Lstrip()
#remove suffix()
#remove sufix()
#index()
#find()
#syntax=variable.method

#upper()
pythonlife = "please subscribe"
print(pythonlife.upper())

x = "my program"
print(x.upper())

#lower()
a = "PYTHON LIFE"
print(a.lower())


x = "WEL COME PYTHON"
print(x.lower())

#ends with

a = "python language"
print(a.endswith("e"))

a = "python language"
print(a.endswith("l"))

#starts with
x ="python language"
print(x.startswith("p"))


x ="python language"
print(x.startswith("a"))

#replace()
s = "my world"
print(s.replace("world","programming"))

s = "this is a aman aman"
a = s.replace("a","b")
print(a)

s = "this is a ayaansh ayaansh"
a = s.replace("a","b")
print(a)

#spliting of string
#spliting is nothing but separate

#s = "this is aman aman"
#l = s.split("i")
#for i in l:
 #   print(i,end='')


s = "python life"
print(s.split(" "))

#count()
s = "python language"
print(s.count("a"))

#r strip()
s = "my program"
print(s.rstrip("program"))
#l strip()
s = "my program"
print(s.lstrip("my"))


#index()
s = "this is aman"
print(s.index("this"))

s = "this is aman"
print(s.index("i"))


s = "this is a aman aman"
print(s.index("raju"))
#find()
s = "this is a aman aman"
print(s.find("raju"))

s = "python program"
print(s.find("raju"))


#type to check char present in the string
#is digit()
#this method returns True if the string contains only numeric digits
#i.e(0-9)else returns false
#syntax = string.isdigit()
#isdiit()
num = "12345"
print(num.isdigit()) #.....>True

name = "123dca456"
print(name.isdigit())#......>False

#isalpha()
#syntax=string.isalpha()
#this method returns True the string contains only alphabetic
#i.e(a-z)(A-Z)at least one char
#else returs False
name = "greekShows"
print(name.isalpha())

#isalnum()
#syntax=string.isalnum(A-Z,a-z,0-9)at least 1 char

msg = "welcome123"
print(msg.isalnum())#...>TRUE

msg = "welcome@123"
print(msg.isalnum())#....>FALSE becoz special char

#isidentifier()
#True:if string is valid identifier .else returns False
#syntax:string.isidentifier

s = "abcdef"
print(s.isidentifier()) #....>o/p true

s = "abc def"
print(s.isidentifier())#....>o/p false

#isspace
#true:if all char are spaces
#syntax = string,isspace()
s = "  "
print(s.isspace())#..>o/p true

s= "  y "
print(s.isspace())#...>o/p false

s = "/t"
print(s.isspace())#...>o/p true

#isupper
name = "GREEKSHOW"
print(name.isupper())

name = "GREEKSHOW"
str1 = name.isupper()
print(name)
print(str1)#....>TRUE

#is lower
name = "greekshow"
print(name.islower())

name = "greekshow"
str1 = name.lowercase()
print(name)
print(str1)#...>O/P TRUE

#istitle
name = "Hello How Are You"
str1 = name.istitle()
print(name)
print(str1)#....>O/P TRUE

name = "Hello How Are you"
str1 = name.istitle()
print(name)
print(str1)#...>o/p False becoz last char used in small letter
