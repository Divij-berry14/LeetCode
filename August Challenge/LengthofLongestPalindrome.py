def LongestPalindrome(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    res = 0
    flag = False
    for i, j in d.items():
        if j % 2 == 0:
            res = res + j
        else:
            res = res + j -1
            flag = True
    if flag:
        res = res + 1
    return res

print(LongestPalindrome("aaaabbbbbbcccddd"))