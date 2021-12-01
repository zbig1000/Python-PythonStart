### Initial Code
import functools

def suppress_exceptions_ex(parameter = Exception, value_on_error = None):
    def decor(func):
        @functools.wraps(func)  #inaczej docu wyswietlane dla wrapera zamiast foo
        def wrapper(*args, **kwargs):
            ''' super wrapper '''
            try:
                return func(*args, **kwargs)
            except parameter:
                result = value_on_error
            return result
        return wrapper    
    return decor   
    ### Expected Behaviour

@suppress_exceptions_ex(ZeroDivisionError, 0.0)
def foo(a, b):
    ''' foo function '''
    return a / b

print(foo(4, 2))
print(foo(4, 0))  # ==> return 0.0
#print(foo('aaa', 'vvv'))  # ==> return another exception

help(foo)