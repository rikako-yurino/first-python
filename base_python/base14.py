# セット
s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

u = s|t #和集合
# u = s.union(t)

print(u)

# 積集合
u = s & t #s.intersection(t)
print(u)

# 差集合
u = s - t #s.difference(t)
print(u)

# どちらか一方に含まれているが両方に含まれていない要素
u = s ^ t #s.symmentric_difference(t)
print(u)

# 要素格納
s |= t
print(s)

#issubset, issuperset, isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t))
print(s.issuperset(t))
print(t.isdisjoint(s))
print(t.isdisjoint(u))