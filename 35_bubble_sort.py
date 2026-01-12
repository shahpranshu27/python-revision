def bubble_sort(elements):
    n = len(elements)
    for i in range(n-1):
        for j in range(n-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                
    return elements

print(bubble_sort([5, 2, 8, 1, 9]))