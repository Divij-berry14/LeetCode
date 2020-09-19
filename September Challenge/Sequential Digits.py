def sequentialDigits(low, high):
    digits = "123456789"
    ll = len(str(low))
    lh = len(str(high))
    res = []
    for i in range(ll, lh + 1):
        for j in range(0, 10 - i):
            num = int(digits[j : j+i])
            if num >= low and num <= high:
                res.append(num)
    return res
low = 100
high = 12000
print(sequentialDigits(low, high))