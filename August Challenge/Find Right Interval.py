# def findRightInterval(intervals):
    # l = len(intervals)
    # if l == 1:
    #     return -1
    # res = []
    # for i in range(l):
    #     min = 100000000
    #     index = -1
    #     for j in range(l):
    #         if intervals[j][0]>=intervals[i][1] and min>intervals[j][0]:
    #             index = j
    #             min = intervals[j][0]
    #     res.append(index)
    # return res

def findRightInterval(intervals):
    sorted = []
    n = len(intervals)
    for i in range(n):
        sorted.append([intervals[i], i])
    sorted.sort()
    print(sorted)
    result = [-1] * n

    def binary_search(x):
        if sorted[n - 1][0][0] < x:
            return -1

        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if sorted[mid][0][0] >= x:
                r = mid - 1
            else:
                l = mid + 1
        return sorted[l][1]

    for i in range(n):
        result[i] = binary_search(intervals[i][1])

    return result

li = [ [3,4], [2,3], [1,2] ]
print(findRightInterval(li))
# print("bv",BinarySearch([1,3,5,6,9],9))



