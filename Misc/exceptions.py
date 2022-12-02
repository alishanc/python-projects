def main():
    x = get_int("What's x? ") # used in 'prompt' param
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) # more reusable
            # return int(input("What's x? "))
            # x = int(input("What's x? "))
        except ValueError:
            pass
            # print("X is not an integer")
        # else:
        #     # break
        #     return x

main()