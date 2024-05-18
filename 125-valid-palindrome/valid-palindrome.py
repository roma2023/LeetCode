class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        we could just generalize the format of all the characters, for example, we can turn everything into a small case strings, then we use two pointers or just compare two ends and shirnk both ends at each step, but the fastest way would be just to reverse the string, then comparing if the reversed equal original
        """

        generalized = list(filter(lambda string: string.isalnum(), s.lower()))
        reverse = generalized[::-1]
        return generalized == reverse