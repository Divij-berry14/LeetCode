def getHint(secret, guess):
    bull = 0
    cow = 0
    secret1 = list(map(int, secret))
    guess1 = list(map(int, guess))
    index = -1
    for i in range(len(secret1)):
        if secret1[i] == guess1[i]:
            bull += 1
            secret1[i] = -1
            guess1[i] = -1
    print(secret1)
    print(guess1)
    d = {}
    for i in secret1:
        if i >= 0:
            d[i] = d.get(i, 0) + 1
    print(d)
    for i in range(len(guess1)):
        if guess1[i] in d and d[guess1[i]] > 0:
            d[guess1[i]] -= 1
            cow += 1

    print(bull, cow)
    res = str(bull) + "A" + str(cow) + "B"
    return res


secret = "1122"
guess = "2211"
print(getHint(secret, guess))