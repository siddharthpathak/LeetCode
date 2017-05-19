#LeetCode: https://leetcode.com/problems/happy-number/



def get_digits(x):
    l = []
    while x:
        temp = x % 10
        l.append(temp)
        x = x/10
    return tuple(l)


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    cycle = {}
    while True:
        temp = get_digits(n)
        new = sum([x*x for x in temp ])
        if new == 1:
            return True
        elif cycle.get(temp,None) is None:
            cycle[temp] = True
            n = new
        else:
            return False
