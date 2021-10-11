

def kth_element(arr1, arr2, k, p1=0, p2=0):

    # p1 is the pointer for arr1 that effectively reduces the size of the array
    # p2 is the pointer for arr2 that effectively reduces the size of the array

    # Catch case where end of arr1 is reached, including if arr1 is empty
    if p1 == len(arr1):
        return arr2[p2 + k - 1]

    # Catch case where end of arr1 is reached, including if arr2 is empty
    if p2 == len(arr2):
        return arr1[p1 + k - 1]

    # Base Case, once k == 1 return the minimum of the array values at their pointers(p1, p2)
    if k == 1:
        return min(arr1[p1], arr2[p2])

    k_div = k//2

    # check if size of arr1 is less than k_div
    if len(arr1) - p1 <= k_div - 1:
        # if the last element in arr1 is less than the current element pointed to in arr2, we have found the value of
        # the kth element
        if arr1[len(arr1) - 1] < arr2[p2 + k_div - 1]:
            return arr2[p2 + k - len(arr1) + p1 - 1]

        # if the last element of arr1 is greater than the current element pointed to in arr2, keep searching for
        # kth element
        else:
            return kth_element(arr1, arr2, k - k_div, p1, p2 + k_div)

    # check if size of arr2 is less than k_div
    elif len(arr2) - p2 <= k_div - 1:

        # if the last element in arr2 is less than the current element pointed to in arr1, we have found the value of
        # the kth element
        if arr2[len(arr2) - 1] < arr1[p1 + k_div - 1]:
            return arr1[p1 + k - len(arr2) + p2 - 1]

        # if the last element of arr2 is greater than the current element pointed to in arr1, keep searching for
        # kth element
        else:
            return kth_element(arr1, arr2, k - k_div, p1 + k_div, p2)

    else:
        # if current element pointed to in arr1 is less than element pointed to in arr2, divide arr1 further
        if arr1[p1 + k_div - 1] < arr2[p2 + k_div - 1]:
            return kth_element(arr1, arr2, k - k_div, p1 + k_div, p2)

        # if current element pointed to in arr1 is greater than element pointed to in arr2, divide arr2 further
        else:
            return kth_element(arr1, arr2, k - k_div, p1, p2 + k_div)




