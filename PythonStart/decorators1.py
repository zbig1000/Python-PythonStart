### Initial Code

test_functions = []

def test(func):
    test_functions.append(func)
    return func



### Expected Behaviour
@test
def a():
    print("a result")
    
@test
def b():
    print("b result")
    
#def c():
#    print("c()")
    
print(test_functions)
assert test_functions == [a, b]

for test_function in test_functions:
 #   print(test_function)
    test_function()

a()
b()
