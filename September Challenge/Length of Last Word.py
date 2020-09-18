def lengthofLastWord(s):
    n = len(s)
    res = 0
    while n > 0:
        n -= 1
        if s[n] != " ":
            res += 1
        elif res > 0:
            return res
        else:
            return res

s = "Hello world"
print(lengthofLastWord(s))