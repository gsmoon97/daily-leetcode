class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} # to store potential matches
        for i in range(len(nums)):
            num = nums[i]
            offset = target - num
            if offset in dict: # to check if current number is a potential match
                return [dict[offset], i]
            dict.update({num : i}) # to add new potential matches