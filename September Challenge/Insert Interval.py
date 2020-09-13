class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i, n = 0, len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        print(result)

        mI = newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            mI[0] = min(mI[0], intervals[i][0])
            mI[1] = max(mI[1], intervals[i][1])
            i += 1

        result.append(mI)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result

intervals = [[1,3],[6,9]]
newInterval = [2,5]
s = Solution()
print(s.insert(intervals, newInterval))
