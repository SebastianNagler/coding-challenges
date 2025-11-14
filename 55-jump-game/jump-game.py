class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = {0}
        queue = [0]
        len_nums = len(nums)
        while queue:
            i = queue[0]
            if i == len_nums - 1:
                        return True
            del queue[0]
            for j in range(min(len_nums - 1, i + nums[i]), i, -1):
                if j not in reachable:
                    queue.append(j)
                    reachable.add(j)
        return False