class Solution:
    def decodeString(self, s: str) -> str:

    # Input: s = "3[a2[c]]"
    # s = 3[acc] => s = accaccacc
    # stack = []
    # stack = [3], open = 1, closed = 0
    # stack = [3a2], open = 2, closed = 0
    # stack = [3a2c], open = 2, closed = 1, start popping from the stack until we see a number
    # temp = "c" * 2 and push it back to the stack
    # stack = [3acc], open = 2, closed = 2, start popping from the stack ubtil we see a number
    # temp = "acc" * 3
    # stack = [accaccacc]
    # at the end string = "accaccacc"

    # Output: "accaccacc"

        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()

                # stack = [13]
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                subs = temp * int(num)
                stack.append(subs)


        return "".join(stack)
                







