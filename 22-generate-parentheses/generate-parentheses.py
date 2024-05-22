class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # use backtracking
        # use stacks
        # time complexity - O(n^2)
        # space complexity - O(n)

        # make stacks
        stack, res = [], []

        # define backtracking func

        def backtrack(openN, closedN):

            # case 1:  we are done
            if openN == closedN == n:
                res.append("".join(stack))
                return 

            # case 2:  need more open pars
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # case 3: need closing pars
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack(0,0)
        return res