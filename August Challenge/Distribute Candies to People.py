def distributeCandies(candies, numPeople):
    li = [0] * numPeople
    c = 2
    count = 1
    indx = 0
    while(candies > 0):
        li[indx] = li[indx] + count
        candies -= count
        indx += 1
        count += 1
        if indx == numPeople:
            indx = 0
        if count > candies:
            count = candies
    return li
print(distributeCandies(10, 3))