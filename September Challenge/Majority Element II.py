# def majorityElement(nums):
#     n = int(len(nums)/3)
#     d = {}
#     res= []
#     for i in nums:
#         d[i] = d.get(i, 0) + 1
#     for key in d:
#         if d[key] > n:
#             res.append(key)
#     return res
#
# nums = [1,1,1,3,3,2,2,2]
# print(majorityElement(nums))


# Using Moore’s Voting Algorithm)
def majorityElement(nums):
    if not nums:
        return []

    # 1st pass
    count1, count2, candidate1, candidate2 = 0, 0, None, None
    for n in nums:
        if candidate1 == n:
            count1 += 1
            print("1", count1)
        elif candidate2 == n:
            count2 += 1
            print("2", count2)
        elif count1 == 0:
            candidate1 = n
            count1 += 1
            print("3", candidate1, count1)
        elif count2 == 0:
            candidate2 = n
            count2 += 1
            print("4", candidate2, count2)
        else:
            count1 -= 1
            count2 -= 1
            print("5", count1, count2)

    # 2nd pass
    result = []
    for c in [candidate1, candidate2]:
        if nums.count(c) > len(nums) // 3:
            result.append(c)

    return result

A = [1,1,1,3,3,2,2,2]
print(majorityElement(A))