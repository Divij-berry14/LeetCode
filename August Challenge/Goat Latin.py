def toGoatLatin(S):
    l = len(S)
    new_s = S.split()
    # print(new_s)
    final_str = ""
    vowels = ["a", "e", "i" , "o", "u","A","I","E","O","U"]
    j = 1
    k = 0
    for i in new_s:
        li = list(i)
        print(li)
        if li[0] in vowels:
            t = "a" * j
            temp = "".join(li)
            if k == 0:
                final_str = final_str + temp + "ma" + t
            else:
                final_str = final_str + " " + temp + "ma" + t
            j = j + 1
            k = k + 1
            li.clear()
            # print(final_str)
        else:
            m = li[0]
            li.remove(li[0])
            t = "a" * j
            li.append(m)
            temp = "".join(li)
            if k == 0:
                final_str = final_str + temp + "ma" + t
            else:
                final_str = final_str + " " + temp + "ma" + t
            li.clear()
            k = k + 1
            j = j + 1
            # print(final_str)
    return final_str

print(toGoatLatin("The quick brown fox jumped over the lazy dog"))