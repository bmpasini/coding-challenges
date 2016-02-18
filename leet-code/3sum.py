# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
# For example, given array S = {-1 0 1 2 -1 -4},
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solutions = list()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                j = i+1
                k = len(nums)-1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    solution = list()
                    if sum == 0:
                        solution.append(nums[i])
                        solution.append(nums[j])
                        solution.append(nums[k])
                        if solution not in solutions:
                            solutions.append(solution)
                        j += 1
                        k -= 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                    elif sum < 0:
                        j += 1
                    else:
                        k -= 1
        return solutions