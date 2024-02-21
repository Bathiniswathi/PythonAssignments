

#inbuilt function
#user defined fuction 

# def wish():
#     print("hello good morning ")

# wish()
# wish()
# wish()
# wish()
# wish()
# wish()
# wish()






# def squ(x):
#     print(x,x*x)


# squ(10)
# squ(20)
# squ(100)
# squ(200)
# squ(3)





# def evnodd(x):
#     if x%2==0:
#         print(x,"even")
#     else:
#         print(x,"odd")


# evnodd(10)
# evnodd(1)


#1.positional arg

# def sub(x,y):
#     print(x-y)

# sub(20,10)


#2.keyword arg

# def wish(age,name,msg):
#     print("hello",name,msg,age)

# wish(20,msg="good bye",name="aman")

#defualt arg

# def wish(name="guest"):
#     print("hello",name," how are you")

# wish()


#variable length arg

# def sum(*a):
#     result=0
#     for x in a:
#         result=result+x
#     print(result)
# sum(10,20,30,40,50,60)


#positional arguments

def add(x,y):
    print(x+y)

    add(20,30)



def sub(x,y):
    print(x-y)

    sub(20,10)


    def mul(x,y):
        print(x*y)

        mul(5,5)


#keyword argument

def wish(age,name,msg):
    print("hello",name,msg,age)

    wish(20,msg="good bye",name="aman")


def my_function(child3,child2,child1):
    print("the youngest child is" + child3)

    my_function(child1="aman",child2="raju",child3="better")



def my_function(fruit3,fruit2,fruit1):
    print("the last fruit is" + fruit3)

    my_function(fruit1="apple",fruit2="orange",fruit3="guva")
    
#default argument

def my_function(country="norway"):
    print("i am from " + country)

    my_function("india")
    my_function("sweeden")
    my_function()
    my_function("oddisha")



def my_function(mobile="oppo"):
    print("my mobile name is " +mobile)

    my_function("apple")
    my_function("i-phone")
    my_function()
    my_function("redmi")


def wish(name="guest"):
    print("hello",name,"how are you")

    wish() 


#variable length
def fun(*x):
    fun(1,2,4) 
    fun()
    fun(5,7)


    def fun(*x):
      for i in x:
        print(i)

def sum(*a):
    result=0
    for x in a:
        result=result+x
        print(result)
        sum(10,20,3,40)       