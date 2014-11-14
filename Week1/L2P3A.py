# Possible solutions:
import random
def deterministicNumber():
    return 10 # or 12 or 14 or 16 or 18 or 20

# or

def deterministicNumber():
    random.seed(0) # This will be discussed in the video "Drunken Simulations"
    return 2 * random.randint(5, 10)