# Using Moore’s Voting Algorithm

def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count += 1
            print("1", count)
        else:
            count -= 1
            print("2", count)
        if count == 0:
            maj_index = i
            count = 1
            print("3", maj_index, count)
    return A[maj_index]


# Function to check if the candidate occurs more than n/2 times
def isMajority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A) / 3:
        return True
    else:
        return False


# Function to print Majority Element
def printMajority(A):
    # Find the candidate for Majority
    cand = findCandidate(A)

    # Print the candidate if it is Majority
    if isMajority(A, cand) == True:
        print("res", cand)
    else:
        print("No Majority Element")

A = [1,1,3,7,2,3,4,9,3,10,11,3,14,3,15,3,3]
print(len(A))
printMajority(A)