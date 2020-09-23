n = input()
a = [i+1 for i in range(0, 9)]
n1 = list(map(int, str(n)))
print(n1)
count = 0
for i in range(1,10):
    n1[i] = n[i]*i


# flag = False
# for i in range(1,10):


