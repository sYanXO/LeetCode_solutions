class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mult=1
        right_mult=1
        n=len(nums)
        l_arr=[0]*n
        r_arr=[0]*n

        for i in range(n):
            j= -i -1
            l_arr[i]=left_mult
            r_arr[j]=right_mult
            left_mult*=nums[i]
            right_mult*=nums[j]

        return [l*r for l,r in zip(l_arr,r_arr)]        
###########################################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))

        prefix= 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix=nums[i]*prefix
        postfix=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=postfix
            postfix=postfix*nums[j]

        return res        



        

        