# https://leetcode.com/problems/monotonic-array/description/

def isMonotonic(self, A):

    len_a=len(A)
    increasing=decreasing=False

    if len_a <= 1:
        return True

    for i in range(len_a-1):
        if A[i] == A[i+1]:
            continue
        if A[i] < A[i+1]:
            increasing = True
            if decreasing:
                return False
        if A[i] > A[i+1]:
            decreasing = True
            if increasing:
                return False

    return True
