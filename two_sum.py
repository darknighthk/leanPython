'''
link proplem: https://leetcode.com/problems/two-sum/
code submit:
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j];
'''

def twoSum(nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
a=twoSum([1,2,3],3)
print(*a)