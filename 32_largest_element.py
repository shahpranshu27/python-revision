def largest(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            
    return largest

print(largest([10, 2, 4, 6, 9]))