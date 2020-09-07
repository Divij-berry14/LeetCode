def wordPattern(pattern, str1):
    d1 = {}
    # if len(pattern) != len(str1):
    #     return False
    str2 = str1.split()
    flag = 0
    val = []
    for i in range(len(str2)):
        if (pattern[i] in d1):
            if d1[pattern[i]] == str2[i]:
                flag = 1
            else:
                return False

        elif str2[i] in val:
            return False

        else:
            d1[pattern[i]] = str2[i]
            val.append(str2[i])
            flag = 1
    print(d1)
    print(val)
    if flag == 1:
        return True
    else:
        return False

print(wordPattern("abba","dog dog dog dog"))


