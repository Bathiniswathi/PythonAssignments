#list

l=list(range(1,10,2))
print(l)

l = list(range(1,20,2))
print(l)
#types of methods
#1.append
#2.extend
#3.remove
#4.pop
#5.count
#6.insert
#7.index

#append
l = [1,2,3,4,"swathi"]
l.append("girl")
print(l)

l = [1,2,3,4,5]
l.append(6)
print(l)

#extend
l = [1,2,3,4,5]
l.extend("swathi")
print(l)

l1 =["apple","banana","cherry"]
l2 =["red","yellow","merun"]
l1.extend("aman")
print(l1)
print(l2)
l1 =["apple","banana","cherry"]
l2 =["red","yellow","merun"]
l2.extend("amanraju")
print(l1)
print(l2)

#remove
l =[10,20,30,40]
l.remove(20)
print(l)

l =[10,20,30,40,50]
l.remove(50)
print(l)

#pop
l =[1,2,3,4]
l.pop(2)
print(l)

l =["aman","raju","rani","bitter"]
l.pop(3)
print(l)

#count
l =[20,40,60,80]
l.count(1)
print(l)

l =[10,20,30,40]
l.count(1)
print(l)

#insert
l =[1,2,3,4]
l.insert(1,2)
print(l)

l =[10,20,30,100]
l.insert(20,100)
print(l)

l =[11,22,33,44,"swathi"]
l.insert(44,"swathi")
print(l)

#index
l =[10,20,30,40]
l.index(100)
print(l)

l =[10,20,30,40]
l.index(100)
print(l)

#list in list
l =[10,20,[30,40],50,60]
print(l(2))

l=[1,20,[3,40],50,60]
print(l[2])
print(l[2][1],l[3])