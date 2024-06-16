# Time: log(min(n, m))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # make count total and half lengths
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # make A a smaller list
        if len(B) < len(A):
            A, B = B, A

        # binary search
        l, r = 0, len(A) - 1
        while True:
            # mid of A
            i = (l + r) // 2  # A
            # idx of B is rest of half 
            j = half - i - 2  # B

            # save the borders of A and B
            # use -& and +& for boundaries oif exceptional cases
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else: # Bleft > Aright
                l = i + 1
