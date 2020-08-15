
def eraseOverlapIntervals(intervals):
    if intervals == []:
        return 0
    intervals.sort(key=lambda x: x[1])
    remove = 0
    end = intervals[0][0]
    for time in intervals:
        start = time[0]
        if start < end:
            remove += 1
        else:
            end = time[1]
    return remove

intervals = [[2, 3], [3, 4], [4, 5], [1,1000]]
print(eraseOverlapIntervals(intervals))