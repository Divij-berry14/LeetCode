def computeLPSArray(string, M, lps):
    length = 0  # length of the previous longest prefix suffix
    i = 1

    lps[0] = 0  # lps[0] is always 0

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # This is tricky. Consider the example AAACAAAA
                # and i = 7.
                length = lps[length - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


# Returns true if string is repetition of one of its substrings
# else return false.
def isRepeat(string):
    # Find length of string and create an array to
    # store lps values used in KMP
    n = len(string)
    lps = [0] * n

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(string, n, lps)

    # Find length of longest suffix which is also
    # prefix of str.
    length = lps[n - 1]

    # If there exist a suffix which is also prefix AND
    # Length of the remaining substring divides total
    # length, then str[0..n-len-1] is the substring that
    # repeats n/(n-len) times (Readers can print substring
    # and value of n/(n-len) for more clarity.
    if length > 0 and n % (n - length) == 0:
        return True
    else:
        False


# Driver program
txt = ["ABCABC", "ABABAB", "ABCDABCD", "GEEKSFORGEEKS",
       "GEEKGEEK", "AAAACAAAAC", "ABCDABC"]
n = len(txt)
for i in range(n):
    if isRepeat(txt[i]):
        print("True")
    else:
        print("False")