class Solution:
    def isValid(self, s: str) -> bool:

        """
        we could keep track of each type of opening and closing parenthesis

        we can add 1 at each opening and add -1 at each closing, then if we detect that the sum is less than 0 at any point that means there are more xlosing than opening parenthesis which means its not valid, so we return false

        Yes, did we cover all the cases? yes

        we can notice that when there is an opening then the only options that should come after it are the closing of the same type or openin gof other types, 

        for example for "(" next ones can be ")" then we are done its valid piece of parentheiss then we can conintue if its "{[(" then the closing parenthesis type should come ij  the same order, hence we can use stacks for this solution 
        
        This is an O(n) work both time and space wise
        
        """
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            # if its the opening par then save it in stack and skip 
            if c not in Map:
                stack.append(c)
                continue
            # if its the closing one then there should 
            # matching opening in the stack
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack