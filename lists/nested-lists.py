list = [1, 2, [0, 9, ['A', 'B']], 4, 5]

print(list)
print(list[2])
print(list[2][2])
print(list[2][2][1])

m1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
m2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
c=[]

for i in range(len(m1)):
    s = []
    for j in range(len(m1[i])):
        s.append(m1[i][j] + m2[i][j])
    c.append(s)

print(c)