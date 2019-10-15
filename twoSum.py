# 解法一，直接在nums里搜索target-num1
class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            tmp = nums[:i]
            if target - nums[i] in tmp:
                j = tmp.index(target-nums[i])
                break
        if j >= 0:
            return [j,i]

# 解法二，利用字典模拟哈希查询
    def twoSum_2(self, nums, target):
        hashmap = {}
        # 创建一个字典将nums的数据和下标映射
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        # 查找
        for i, num in enumerate(nums):
            j = hashmap.get(target-num)
            if i != j and j is not None:
                return [i, j]




s = Solution()
print(s.twoSum_2([0,4,3,0],0))


# l = map(fun, [2, 7, 11, 13],[9]*4)
# l = list(l)
