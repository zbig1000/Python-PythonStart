def generate_adder(x):
    def add(y):
        return x + y
    return add
add_5 = generate_adder(5)
print(add_5)  # add_5 == add, assuming x = 5
print(add_5(10))
print(generate_adder(5)(10))
print(generate_adder(5))

#print(generate_adder(5, 10))  # ==> TypeError
