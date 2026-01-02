s={1,2,3,4,5}
e={4,5,6,7,8}
print(s)
print(e)
print('union=',s|e)#one element print one time
print('union=',s.union(e))
print("intersection= ",s&e)#print only comman elements
print('intersection = ',s.intersection(e))
print('difference=',s.difference(e))#Elements in A but not in B
print("difference=",s-e)
print('Symmetric Difference=',s^e)#Elements not common in both sets
a={10,20,30,40}
a.add(50)
print(a)
a.remove(50)
print(a)