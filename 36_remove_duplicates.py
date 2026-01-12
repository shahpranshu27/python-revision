def remove_duplicate(arr):
    unique_nums = []
    for num in arr:
        if num in unique_nums:
            continue
        else:
            unique_nums.append(num)
    return unique_nums

print(remove_duplicate([1, 2, 3, 2, 1, 3, 2, 4, 5, 4]))