class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplet_pairs = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            pairs = self.pairs_sorted_sum_all(nums, i+1, -nums[i])
            for pair in pairs:
                triplet_pairs.append([nums[i]]+pair)
        return triplet_pairs

    def pairs_sorted_sum_all(self, nums, start, target):
        left, right = start, len(nums)-1
        pairs = []
        while left < right:
            sums = nums[left]+nums[right]
            if sums == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif sums < target:
                left += 1
            else:
                right -= 1
            
        return pairs

