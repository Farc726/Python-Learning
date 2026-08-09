s1={4,8,6,9,7,3,7,4}
print(type(s1))
#无序 自动去重
print(s1)

s2=set()
print(s2)
print(type(s2))

s={100,200,300,400,500,600}
s.add(999)
print(s)

s.remove(100)
print(s)

e=s.pop()
print(e)
print(s)

s.clear()
print(s)

s2={1,2,3}
s3={2,3,4}
print(s2.difference(s3))
print(s3.difference(s2))
print(s2.intersection(s3))
print(s2.union(s3))