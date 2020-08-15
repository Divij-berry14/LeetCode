class Solution:
    def combinationSum(self, candidates, target):

        out = []
        self.backtracking(out, [], candidates, target, 0)

        return out

    def backtracking(self, out, curr, candidates, target, idx):
        if target < 0:
            return
        if target == 0:
            out.append(curr)
            return

        for i in range(idx, len(candidates)):
            print(curr+[candidates[i]])
            self.backtracking(out, curr + [candidates[i]], candidates, target - candidates[i], i)

li = [2, 3, 6, 7]
target = 7
s=Solution()
print(s.combinationSum(li,target))



