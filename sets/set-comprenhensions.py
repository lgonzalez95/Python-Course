s1 = {x for x in range(10)}
print(type(s1))
print(s1)


s2 = {x*2 for x in [-2, 0, 2, 4]}
print(type(s2))
print(s2)


s3 = {x.upper() for x in 'philippines'}
print(type(s3))
print(s3)