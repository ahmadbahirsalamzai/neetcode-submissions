class Solution:
    #time o(n), space: o(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left array works as our resutls arry, after storing left values we would mutate it to be multiplied by the right values and have the ptotal product excluding itself
        left  = [1]*len(nums)
        running_product = 1
        for i in range(len(nums)):
            temp = nums[i]
            left[i] = running_product
            running_product = running_product*temp
        #print(left)
        right = [1]*len(nums)
        running_product = 1
        for i in range(len(nums)-1, -1, -1):
            temp = nums[i]
            right[i] = running_product
            running_product = running_product*temp
        #print(right)
        for i in range(len(nums)):
            left[i] = left[i]*right[i]

        return left