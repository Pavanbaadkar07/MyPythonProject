a=[]
print("List at starting")
print(a)
a.append(10)
print("After adding 10 to a list")
print(a)
a.extend(["Pavan",50])
print("After adding Pavan and INT(50) to a same list")
print(a)
a.insert(4,60)
a.extend(["raksan",0,"car",100])
a.insert(3,"hero")
print("After adding  Word hero to 3rd index in a same list")
print(a)
mixone=[]
mixtwo=[]
print("mixone=",a[1::2])
print("mixtwo=",a[2::2])
for item in a:
    if isinstance(item,(int,float)):
        mixone.append(item)
    else:
        mixtwo.append(item)