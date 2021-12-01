def dict_without_Nones(**kwargs):
    local = {}
    for k, v in kwargs.items():
        if v is not None:
            local[k] =v
    return local
    

print(dict_without_Nones(a="1999", b="", c=None))
print(dict_without_Nones(a="1999", b=None, d=None))
