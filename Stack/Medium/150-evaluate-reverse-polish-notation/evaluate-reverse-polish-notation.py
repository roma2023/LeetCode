class Solution:
    # Complexity Analysis
    # As we just itertae through the list and pop-push
    # Time Complexity = O(n)
    # And as we save all in stack
    # Space Complexity = O(n) 
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for i in tokens:
            if i not in ops:
                stack.append(i)
                continue
            else:
                if i == "+":
                    val1 = int(stack.pop())
                    val2 = int(stack.pop())
                    stack.append(val1+val2)
                elif i == "-":
                    val1 = int(stack.pop())
                    val2 = int(stack.pop())
                    stack.append(val2-val1)
                elif i == "*":
                    val1 = int(stack.pop())
                    val2 = int(stack.pop())
                    stack.append(val1*val2)
                elif i == "/":
                    val1 = int(stack.pop())
                    val2 = int(stack.pop())
                    stack.append(val2/val1)
        return int(stack.pop())
                
        