class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #3 sum lets see what to do for this
        # naive would be to have 3 pointers and then iterate through each possible possibility and then return the results of adding up
        # two sum + 1 what if did two numbers then with result see if target - twosum = res see if res is found then store saves on one loop?
        # its == 0 search for complement after two sum
        ans = []
        nums.sort()
        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans