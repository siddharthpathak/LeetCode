"""
Contains Bubble Sort, Insertion Sort, Selection Sort and Merge Sort.
To - Do: Shell Sort and Quick Sort
"""




def bubble_sort(L):
    """
        Sort a list L using bubble sort.
        Complexity: O(n^2)
    """
    exchanges = True
    while exchanges is True:
        exchanges = False
        for j in range(1,len(L)):
            if L[j-1] > L[j]:
                exchanges = True
                L[j],L[j-1] = L[j-1],L[j] 
    return L


def selection_sort(L):
    """
        Sort a list using Selection Sort
        Complexity: O(n^2)
    """
    suffix = 0
    while suffix != len(L):
        for i in range(suffix+1,len(L)):
            if L[suffix] > L[i]:
                L[suffix],L[i] = L[i],L[suffix]
        suffix +=1
    return L


def merge(left,right):
    result = []
    i,j=0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    while i < len(left):
        result.append(left[i])
        i +=1
    while j < len(right):
        result.append(right[j])
        j +=1
    return result


def merge_sort(L):
    """
        Sort a list L using Merge sort.
        Complexity: O(nLogn), but uses extra space
        Also, slice operator O(K) can be removed
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])       
        right = merge_sort(L[middle:])
        return merge(left,right)


def insertion_sort(L):
    """
        Sort a list using Insertion Sort
        Complexity: O(n^2)
    """
    for i in range(1,len(L)):
        currentValue = L[i]
        position = i
        while position > 0:
            if currentValue < L[position-1]:
                L[position] = L[position -1]
                position -=1
            else:
                break
        L[position] = currentValue
    return L


def test():       
    assert bubble_sort([1,2,3,4,5]) == [1,2,3,4,5]
    assert bubble_sort([5,4,3,2,1]) == [1,2,3,4,5]	
    assert bubble_sort([7,9,100,500,99,10]) == [7,9,10,99,100,500]
    assert insertion_sort([1,2,3,4,5]) == [1,2,3,4,5]
    assert insertion_sort([5,4,3,2,1]) == [1,2,3,4,5]	
    assert insertion_sort([7,9,100,500,99,10]) == [7,9,10,99,100,500]
    assert selection_sort([1,2,3,4,5]) == [1,2,3,4,5]
    assert selection_sort([5,4,3,2,1]) == [1,2,3,4,5]	
    assert selection_sort([7,9,100,500,99,10]) == [7,9,10,99,100,500]
    assert merge_sort([1,2,3,4,5]) == [1,2,3,4,5]
    assert merge_sort([5,4,3,2,1]) == [1,2,3,4,5]	
    assert merge_sort([7,9,100,500,99,10]) == [7,9,10,99,100,500]
    assert bubble_sort([54,26,93,17,77,31,44,55,20]) == insertion_sort([54,26,93,17,77,31,44,55,20]) \
    == selection_sort([54,26,93,17,77,31,44,55,20]) == merge_sort([54,26,93,17,77,31,44,55,20])
    print "test cases passed"

    
if __name__ == "__main__":
    test()
    
