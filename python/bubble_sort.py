def bubble_sort(array, size=-1):
    if size < 0:
        size = len(array)
    if size == 0 or size == 1:
        return array
    for i in range(size-1):
        a, b = array[i], array[i+1]
        if a > b:
            array[i], array[i+1] = b, a

    return bubble_sort(array, size-1)
