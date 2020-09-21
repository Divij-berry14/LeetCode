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

trips = [[3,2,7],[3,7,9],[8,3,9]]
capacity = 11
print(carPooling(trips, capacity))

