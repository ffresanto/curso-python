t1 = (1, 2, 3, 'a', 'Luiz Otávio')

print(t1[2:])

for v in t1:
    print(v)

t2 = 1, 2, 'a', 'b'
print()
print(t2)

t3 = 1, 2, 3, 4, 5
t4 = 6, 7, 8, 9, 10
t5 = t3 + t4
print()
print(t5)

n1, n2, n3, *_ = t5

print(n3)

t10 = (1,2,3,4,5)
t10 = list(t10)
t10[1] = 3000

t10 = tuple(t10)

print(t10, type(t10))