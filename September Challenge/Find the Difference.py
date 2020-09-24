def findtheDiff(s, t):
    s1 = list(s)
    s1.sort()
    t1 = list(t)
    t1.sort()
    if len(s1) != len(t1):
        s1.append(0)
    print(s1, t1)
    for i in range(len(t1)):
        if s1[i] != t1[i]:
            print(t1[i])

s = "abcd"
t = "abcde"
findtheDiff(s, t)