import random
import pi_module

# print "pi" variable from imported "pi_module" referenced above
print(pi_module.pi)
print(pi_module.earth_surface)

# random int
random_integer = random.randint(1, 10)
print(random_integer)

# "random float from [0, 1] 0.000000 -> 0.99999999
random_float = random.random()
print(random_float)

# random float from 0 - 5
y = random_float * 5
print(y)

score = random.randint(0, 100)
print(f"Your score is {score}")
