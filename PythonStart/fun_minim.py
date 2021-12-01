def min_func(*item):
    if not item:
        raise TypeError

    local_min = item[0]
    for i in item:
        if i < local_min:
            local_min = i
    return local_min

print(min_func(22,13,5,7))
print(min_func())


    
