def maxmin(array):
    maxmin = [array[0], array[0]]
    for num in array:
        if num > maxmin[0]:
            maxmin[0] = num
        if num < maxmin[1]:
            maxmin[1] = num
    return maxmin
