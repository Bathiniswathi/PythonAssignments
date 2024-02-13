#tuple data structures
t = (10,20,30,40)
print(len(t))

t = (20,30,40,50)
print(len(t))

#index
t = (20,40,'abc',60)
t.index(20)



t = (2,2,1,'z',3,4,5,6,5)
t.count(2)
print(t.count(2))

#count()
t = (33,4,5,'a','z','b','z',4)
t.count(4)
print(t.count(4))
print(t.count('z'))



t =(33,4,5,'abc',5)
print(t.count(33))

#sorted()


x = (8,3,5,1,7,4,1)
print(sorted(x))

#tuple packing and unpacking
#packing ==>groping into single
a = 10
b = 20
c = 30
d = 40
f =a,b,c,d
print(f)


a = 20
b = 30
c = 40
d = 50
f =a,b,c,d
print(f)


#unpacking tuple
t = (10,20,30,40,50)
a,b,c,d,e=t
print(a,b,c)

t = (1,1,2,3,4)
a,b,c,d,e=t
print(a,b,c)


#set{}
s ={10,20,30,40,40,50,60,60}
print(s)

s ={10,20,30,40}
s.add()
s.update(20,3,4,5,67,8,9,10,50,30,20,60,8)
#you can take a sequence of elements
print(s)

#copy()#to create a clone objects
s1 = {10,20,30,40}
s2 = s1.copy()
print(s2)

s1 = {1,2,3}
s2 = s1.copy()
print(s2)


#pop
s = {10,2,30,4}
print(s.pop())


s = {1,1,2,3,4}
print(s.pop())

#remove()
s = {10,20,30,40,50}
s.remove(100)
print(s)

s = {1,1,2,3}
s.remove(4)
print(s)

#discard

s = {10,30,40,50,60}
s.discard(140)
print(s)

#clear()
s = {10,20,30,50,60}
s.clear()
print(s)





#set.discard(),.remove()&.pop()

#s.remove(x)
#this opreation removes elementx from the set.if element x does not exist,it raises a 
#key error.the.remove(x) opretion returns none

#ex:

s = set([1,2,3,4,5,6,7,8])
s.remove(5)
print(s)

set([1,2,3,4,5,6,7,])
s.remove(4)

#s.discard(x)
#this opreation also removes element x from the set.
#if element x does not exist,it does not raise a key error
#the.discard(x)n opreation returns none
s = set([1,2,3,4,5,6,7])
s.discard(5)
print(s)

set([1,2,3,6,7,8,9])
s.discard(0)

#pop()
#this opreation removes and returns an arbitrary element from the set
#if there are no elements to remove,it rasises a key error
s = set([1])
print.pop()

print(s)
set([])









