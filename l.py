data={10,50,3.25, 10,"Python"}
print(data)
print(type(data))
tech=set()
print(type(tech))
user={}
print(type(user))
data.add(100)
print(data)
data.update([200,"Java",3.50])
print(data)
a={1,5,7,10}
b={10,15,6,8}
print(a|b)
print(a.union(b))
print(a&b)
data={"tech":"python", "version":3.14,}
print(data)
print(type(data))
data["tech"]="java"
print(data)
data["year"]=1991
print(data)
data.update({"tech1":"C Launguage", "year":1991})
# data.clear()
# print(data)
data.pop("version")
print(data)
for key in data.keys():
    print(key)
for values in data.values():
    print(values)
for keys, values in data.items():
    print(f"{keys}={values}")