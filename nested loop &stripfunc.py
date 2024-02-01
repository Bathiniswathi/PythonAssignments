#transfer statements
#1.break
#2.continue
#3.pass
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
  



cars = ["BMW", "Innova","honda"]
for x in cars:
  print(x)
  if x == "Innova":
     break
  

#range
  for x in range(6):
    if x == 3:break
    print(x)
  else:
    print("finally finished") 

#continue:

    fruits = ["apple","banana","cherry"]
    for x in fruits:
      if x == "banana":
        continue
      print(x) 


      leafs = ["mint","coriander","curryleaf"]
      for x in leafs:
        if x == "leafs":
          continue
        print(x) 

 #pass:
                  
  for x in [0, 1, 2]:
   pass

# having an empty for loop like this, would raise an error without the pass statement


#strip()
  city=input("enter the city name")
  list=["hyd","banglore","mumbai","gova"]
  if city.strip() in list:
    print("yes it is availble")
  else:
    print(city,"not availble")

#strip
a= "hello world"
print(a.strip())



fruits=input("enter the fruits name")
list=["apple","banana","cherry"]
if fruits.strip() in list:
  print("yes it is availble")
else:
  print(fruits,"is not availble")

  #lstrip:
  a = "hello world"
  print(a.lstrip("h"))

  x = "my programer"
  print(x.lstrip("my"))


 #rstrip:
  a ="MY PYTHON"
  print(a.rstrip("PYTHON")) 

  x="PYTHON LIFE"
  print(x.rstrip("LIFE"))
               
 



