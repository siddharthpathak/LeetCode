def binary_search(L,key):
    """
        Returns true if the key is found in the list else returns false
        Complexity = O(logn)
        
    """
    first = 0
    last = len(L)-1
    while first <=last:
        middle = (first + last) //2
        if L[middle] == key:
            return True
        else:
            if key < L[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return False


def binary_search_recursive(L,low,high,key):
    """
        Returns true if the key is found in the list else returns false
        Complexity = O(logn)
        Implentation is in recursive manner        
    """
    if len(L) == 0:
        return False
    if (low==high):
        return L[low] == key
    mid = low +(high-low)//2
    if (L[mid] == key):
        return True
    if key < L[mid]:
        return binary_search_recursive(L,low,mid-1,key)
    else:
        return binary_search_recursive(L,mid+1,high,key)
    
def test():       
    assert binary_search_recursive([1,2,3,4,5],0,4,5) == True
    assert binary_search_recursive([0]*256,0,255,5) == False
    assert binary_search_recursive([],0,0,5) == False
    assert binary_search_recursive([1,2,3,4,5],0,5,1) == True
    assert binary_search_recursive([1,2,3,4,5] + [3] * 900,0,904,77) == False
    assert binary_search([1,2,3,4,5],5) == True
    assert binary_search([0]*256,5) == False
    assert binary_search([],5) == False
    assert binary_search([1,2,3,4,5],1) == True
    assert binary_search([1,2,3,4,5] + [3] * 900,77) == False
    print "test cases passed"

    
if __name__ == "__main__":
    test()



       
    
