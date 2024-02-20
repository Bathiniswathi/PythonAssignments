#Types of arguments
#1.default arg
#2.keyword arg
#3.variable length arg

#default arg
''''''''
#default arg ahs a default value.it will use in the absence
#of passing values at the time of calling

def fun(x =10,y = 30):
    c =x+y
    print("result is =:",c)


    fun(89,9)
    fun()


#keyword argument
#keyword argument is used to  pass the values with name of variable
#so that we can pass values without bothering the sequence of parameter

#    def fun(x,y):
 #       fun(y=30,x=50)
        


def fun(x,y):
    c = x+y
    print("result is =:",c)

    fun(x = 87,y=90)
    fun(y=40,x=30)#sequnce does't matter


#variable length argument
#in this we can pass arguments in different number of arguments  in different 
 #function call.it will handle all the arguments using pointer.

    def fun(*x):
        fun(1,2,4)
        fun()
        fun(5,7)


    def fun(*x):
      for i in x:
        print(i)



        fun(1,2,3,4)

        fun(4,5)

        fun("vikas","singh")     

