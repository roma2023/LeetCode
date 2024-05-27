class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        left, right = 0, len(nums) - 1
        
        two_sum_list = []
        while left < right: 
            
            sum = nums[left] + nums[right]

            if sum > target: 
                right -= 1
            elif sum < target: 
                left += 1
            else: 
                two_sum_list += [[nums[left], nums[right]]]
                # case of [-2, 0, 0, 2, 2]
                left += 1
                while nums[left-1] == nums[left] and left<right:
                    left += 1
        return two_sum_list
        
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        just to clarify what is the range of the list we are  working with? Are we working strcitcly with inegeres? Are there negative numbers or 0? 
        Hmm, 

        Well, the brute force solution that comes to my mind is just nested looping three times and finding all permutations of triplets that would sum up to 0 right? But this is very costly, as a matter of fact this would be O(n^3) time complexity.

        But, I can think of another approach. If we know that three of them sum up to 0, doesnt this mean that the sum of the two gonna be equal to negative of the thrid one, yeah I guess this is much clearer in mathematical equation

        So, if we have numbers a + b + c = 0 
        a + b = -c   
        a + c = -b 
        b + c = -a 

        how can we leverage this fact? hmm let me think

        so I think we could go over the the number and keep track of visited numbers in a set as well as different sums that can be made

        for example, let's look at the sample input
        nums = [-1, 0, 1, 2, -1, -4] 
        i, j two pointers
        let's say i is the beginning and j is the end 

        and as we go we keep the visited i and j values in the set
        at first i = -1 and j = -4 

        then check if 5 in the set()
        no, move the greater one and add it to the set => set(-1) 

        and i = 0 and j = -4, is there a 4 in the set, no
        move 4 into set => set(-1, 0)

        and i = 
        => sums_set(-1) 0
        => sums_set(-1, 0) 1
        => sums_set(-1, 0, 1) 2 

        So, apparently there is no better way than first sorting the list in nlogn
        then taking each negative of element as a target and just doing two sum algorithm on the rest of the list, yes let's do this
        ask more about edge cases, think creatively, dont jump into solution right away
        So the time complexity of this algorithm is nlogn for sorting, and n^2 for the looping and calling the helper fucntion, so overall O(n^2)

        space complexity is O(n) because the orting might take up some space depending on the type of sorting being done, but if no space we still use space for two_sum, which in worst case might turn into list of n unique lists cause we are not taking duplicates
        """

        # sorting
        nums.sort()

        three_sum_list = []
        two_sum_list = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            target = -nums[i]
            two_sum_list = self.twoSum(nums[i+1:], target)
            if not two_sum_list:
                continue
            for two_sum in two_sum_list:
                three_sum_list += [[nums[i]] + two_sum]
        return three_sum_list 

