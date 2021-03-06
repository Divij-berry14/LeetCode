# import collections
# def carPooling(trips, capacity):
#     trip_capacity = collections.defaultdict(int)
#     print(trip_capacity)
#     for i in range(len(trips)):
#         no = trips[i][0]
#         start = trips[i][1]
#         dest = trips[i][2]
#         for j in range(start, dest):
#             trip_capacity[j] += no
#             print(trip_capacity)
#             if trip_capacity[j] > capacity:
#                 return False
#     return True

def carPooling(trips, capacity):
    timestamp = []
    for trip in trips:
        timestamp.append([trip[1], trip[0]])
        print(timestamp)
        timestamp.append([trip[2], -trip[0]])
        print(timestamp)
    print(timestamp)
    timestamp.sort()
    print(timestamp)
    used_capacity = 0
    for time, passenger_change in timestamp:
        used_capacity += passenger_change
        print(used_capacity)
        if used_capacity > capacity:
            return False
    return True

# from collections import defaultdict
# def carPooling(trips, capacity):
#     """
#     :type trips: List[List[int]]
#     :type capacity: int
#     :rtype: bool
#     """
#     d = defaultdict(lambda: 0)
#     for trip in trips:
#         num, start, end = trip
#         d[start] += num
#         d[end] -= num
#         print(d)
#     print(d)
#     l = [amount for _, amount in sorted(d.items())]
#     print(l)
#     count = 0
#     for amount in l:
#         count += amount
#         if count > capacity:
#             return False
#     return True

trips = [[3,2,7],[3,7,9],[8,3,9]]
capacity = 11
print(carPooling(trips, capacity))

