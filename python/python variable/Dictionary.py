data={'name':'siddharth','age':20,'dept':'aiml'}
print(data)
print(data['name'])
print(data.get('age'))
data['collage']='amgoi'    #  add element 
print(data)
data['age']=21
print(data)
data.pop('age')# remove element 
print(data)
print(data.keys())# display all keys eg. 'name'
print(data.values())# display all values in dict eg.' siddharth'
di=data.copy()  
print(di)