### Initial Code

def suppress_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:
            result = None
        return result
    return wrapper    
### Expected Behaviour

@suppress_exceptions
def foo(a, b):
    return a / b

print(foo(4, 2))
print(foo(4, 0))  # ==> return None instead of an exception