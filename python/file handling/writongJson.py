import json
data={
    "name":"siddharth",
    'age':21,
    'skill':['python','ai','ml']
}
with open("data.json",'w')as file:
    json.dump(data,file,indent=4)