class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res  = [1]*len(nums) # create the left producnt and store it in res -- we would later modify it to have correct values and return it
        running_product = 1
        for i in range(len(nums)):
            temp = nums[i]
            res[i] = running_product
            running_product = running_product*temp
        #print(res)
        # use the given nums array to store the right product

        running_product = 1
        for i in range(len(nums)-1, -1, -1):
            temp = nums[i]
            nums[i] = running_product
            running_product = running_product*temp
        #print(nums)

        for i in range(len(nums)):
            product = res[i] * nums[i]
            res[i] = product

        return res