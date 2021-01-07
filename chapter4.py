def my_sum(arr):
    if arr == []:
        return 0
    return arr[-1] + my_sum(arr[:-1])

def my_count(arr):
    if arr == []:
        return 0
    return 1 + my_count(arr[:-1])

def my_max(arr):
    if arr == []:
        return -float('inf')
    return arr[-1] if arr[-1] > my_max(arr[:-1]) else my_max(arr[:-1])
        
