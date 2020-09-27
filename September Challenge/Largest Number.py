class LargerNumKey(str):
    def __lt__(x, y):
        print(x, y)
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        print(largest_num)
        return '0' if largest_num[0] == '0' else largest_num

nums = [3,30,34,5,9]
m = Solution()
m.largestNumber(nums)