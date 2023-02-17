class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue  #basically if its not the first element and still it is equal to a then we ignore it and continue to next first element
            
            l, r = i+1, len(nums)-1  #two pointer approach starts
            
            while l<r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1 #we only need to update one of these t0 find the next triplet as the above two if and elif contions will update the other ptr ie. [-2,-2,0,0,2,2], so if l = -2, r = 2, so we got 0 now we update l += 1 it goes to -2 but duplicate hence continue and l = 0, now  l+r > target(0) hence r -= 1, becomes 2, still > 0, hence r -=1, r = 0, otice how only updating one pointer updates the second ptr due to the twi conditions up there
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res 
