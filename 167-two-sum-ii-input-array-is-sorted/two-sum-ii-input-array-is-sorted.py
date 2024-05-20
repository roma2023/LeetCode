class Solution:
    # Complexity Analysis
    # TC = O(n) and SC = O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Hmm, just to clarify are we working with only inteegrs, can there be floats? What range of integers we are working with? negative numbers or zero?

        Hmmm, the brute force solution would be permuting over all possible pairs of number, however, this is not very efficient, in factt= this would result in O(n^2) complexity

        We dont want that at google, can we do better? well if we know that the list is sorted in non decreasing order that means, the max sum of pair we can get should be at the end of the lust and min sum of the pair should be at the beginning right? Hmm how can we leverage this property? Well we could make a pointer to the start and the end. 

        If the sum of two number at these indices are greater than the target, then we could move the right pointer to its left neoght whcih we know is for sure either less than or equal to previous right, else if the sum is less than the target then we could move the left pointer a bit to right, else we know the sum equal target and we will just return the left and right indices.

        let's visualize it here:
        so, if we have a list, let's say:
        [2,7,11,15] => left = 0 and right = 3 => then sum = 2+15 = 17, we see its greater than 9, then now we can decrement right by 1, now left = 0 and right = 2 then sum = 2+11 = 13, 
        this is again greater than 9 and we can decrement right again. left = 0 and right = 1, sum = 9 now it equals the target, hence we can just return [left, right]

        Complexity wise, the time complexity it takes is bound by O(n) linear work because we go through the whole list only once

        Space complexity is constant cause we are creating any new space for a data structure
        Let's code it up now

        just to clarify can we have a list with no such pair, ok, what do we need to return in that case?
        """

        left, right = 0, len(numbers) - 1
        Sum = 0
        while True: # just to clarify could there be no such pair, or will be one
            Sum = numbers[left] + numbers[right]
            if Sum > target: 
                right -= 1
            elif Sum < target: 
                left += 1
            else: 
                return [left + 1, right + 1]  
