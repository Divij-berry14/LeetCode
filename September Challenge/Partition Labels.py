from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        end_ix = [0]*26
        for i in range(len(S)):
            end_ix[ord(S[i]) - ord('a')] = i
        # print(end_ix)
        start = 0
        end = 0
        result = []
        for i in range(len(S)):
            end = max(end, end_ix[ord(S[i]) - ord('a')])
            if i == end:
                result.append(i-start+1)
                start = i + 1
        return result

s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
