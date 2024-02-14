# #union
# # this will return common elements from the two sets

 s1 = {10,20,30,40,50,60,70,80}
 s2 = {10,20,40,90,100,110,120,130}
 print(s1.union(s2))
 print(s1|s2)

# #intersection
 s1={10,20,30,40,50,60,70,80}
 s2={10,20,40,90,100,110,120,130}
 print(s1.intersection(s2))

# #diffrence
 s1={10,20,30,40,50,60,70,80}
 s2={10,20,40,90,100,110,120,130}
 print(s1.difference(s2))


# #sysmetric diff

 s1 = {10,20,30,40,50,60,70,80}
s2 = {10,20,40,90,100,110,120,130}
print(s1.symmetric_difference(s2))



 s={x*x for x in range(12) if x%2==0}
 print(s)


#dict data type 
 d={}
 d=dict()
 d[key]=value
 print(type(d))

 d={}
 name=input
 marks=input
 d[100]=99
 d[200]=88

 print(d)
 print(d[100])

#how to update the dictionaris 

 d={100:"aman",200:"raju",300:"ram"}
 d[800]="laxhman"
 print(d)


#delete elements from dict

 d={100:"aman",200:"raju",300:"ram"}
 del d[100]
 print(d)

 d={100:"aman",200:"raju",300:"ram"}
 d.clear()

 print(d)





#imp fun /methods of dict

 l=((100,"aman"),(200,"raju"))
 d=dict(l)
 print(d)

 d={100:"aman",200:"raju",300:"ram"}
 print(len(d))



#get()
 d={100:"aman",200:"raju",300:"ram"}
 print(d.get(100))
 print(d.get(800))
 print(d[800])

#pop()
 d={100:"aman",200:"raju",300:"ram"}
 print(d.pop(200))


# popitem
 d={100:"aman",200:"raju",300:"ram"}
 print(d.popitem())

#keys()
 d={100:"aman",200:"raju",300:"ram"}
 print(d.keys())

# #vales
 d={100:"aman",200:"raju",300:"ram"}
 print(d.values())

#items() (k,v)
 d={100:"aman",200:"raju",300:"ram"}
 l=d.items()
 print(l)

# #copy()
 d={100:"aman",200:"raju",300:"ram"}
 d1=d.copy()
 print(d1)


#set defualt

 d={200:"raju",300:"ram"}
 print(d.setdefault(100,"sunny"))
 print(d)


