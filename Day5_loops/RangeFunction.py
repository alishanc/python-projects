# Using steps in range function i.e. (0, 10, 2)
for number in range(1, 11, 3):
    print(number)

# Add up to 101
total = 0
for n in range(1, 101):
    total += n
    # add every # in range to total, from 1 - 100
print(total)

# Add even numbers
total = 0
for i in range(2, 101, 2):
    total += i
print(total)
# indentaton of print matters, test and try out

# Using Modulo % and if
total2 = 0
for i in range(1, 101):
    if i % 2 == 0:
        total2 += i
print(total2)