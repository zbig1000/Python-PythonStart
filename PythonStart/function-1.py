list_to_update = []


def append_func(appended_val, list_internal=None  ):
    if list_internal is None:
        list_internal = []
#    else:
    list_internal.append(appended_val)
    return (list_internal)
 
#print(append_func('e', list_to_update2))
#print(append_func('j', list_to_update2))

print(append_func('e'))
print(append_func('j'))
print(append_func('j', ['a','b']))
#print(append_func(['j', 'k'], list_to_update2))
