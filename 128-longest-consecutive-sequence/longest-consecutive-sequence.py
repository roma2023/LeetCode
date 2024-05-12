class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        given an array of integers nums, return the length of the longest consecutive elements sequence? So just to clarify what do you mean by consecutive elements sequence? is it like 1,2,3,4 or is it like the adjacent consecutive elements in the list? 

        Ohhh ok, if the nums imput is like [100,4,200,1,3,2] => 4 because the LCES is 1,2,3,4 and its length is 4.

        Ok, ok, are we working with positive integers only? is the list unsorted?

        the brute force solution that comes to my mind immediately is first sorting the list, then going over the list in O(n) and counting the max length of consecutive elements, however, sorting takes nlogn time complexity, which might be quite expensive and the question is asking to implement this in O(n). Can we do better? 

        so I think we could use a set and whenever we see value right, we can just add both val-1 and val+1 into the set, and if there is a next val that equals one of them that means they should be consequtive. So, [100,4,101,1,3,2, 99] => set(99,101) => set(99, 101, 5, 3) => set(99,101,5,3,0,2) => set(99,101,5,3,0,2,4) =>
        ((98,102), (1,5), (0,3) ) => ((98, 102), (0,5))

        So, we naturally look at it and identify that there are like 3 sequences right, but how to find them, and code them up. So, we can see that each sequence ha sa starting point, starting point is a number in the list that has no left adjacent neighbor in the list, from there we could just mark it as a start of the sequnec and try to find the rest of the sequence. Remember set has an instant access time because of its property. Then w ecan turn our list into a set, [100,4,200,1,3,2] => set(100,4,200,1,3,2) 
        then we iterate through each number and check if its left neigbor there is 99 in set, no then mark 100 as a start of the sequence and start the counter, if not countinue with the next, then check if 101 is in the set, no then counter stops and we wanna record the max then when we reach 1, we see 0 isnt in the set and 2 is in the set count+1, 3 and 4 also in, then 5 isnt then stop the counter, and record it
        """

        Set = set(nums)
        Max = 0
        for num in nums:
            counter = 0
            if num-1 not in Set: 
                while num+counter in Set:
                    counter += 1
            Max = max(Max, counter)
        return Max

"""
complexity analysis, time complexity O(n) we will go over the list at most twice
space complexity, as we are creating a set of the size n, the complexity is O(n)
"""
