def num_gen(n):
    for i in range(n):
        yield i

for i in num_gen(10):
    print(i)