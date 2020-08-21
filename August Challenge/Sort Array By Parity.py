def SortArrayParity(A):
    l = len(A)
    # li = [0] * l
    # start = 0
    # end = l - 1
    # for i in range(l):
    #     if arr[i] % 2 == 0:
    #         li[start] = arr[i]
    #         start = start + 1
    #     else:
    #         li[end] = arr[i]
    #         end = end - 1
    # return li
    j = 0
    for i in range(l):
        if A[i] % 2 == 0:
            A[i], A[j] = A[j], A[i]
            j = j + 1
    return A
arr = [int(x) for x in input().split()]
print(SortArrayParity(arr))