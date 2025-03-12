import random

def generate_random_number(start, end):
    return random.randint(start, end)

start = int(input("Enter the starting value of the range: "))
end = int(input("Enter the ending value of the range: "))

random_number = generate_random_number(start, end)

print(f"A random number between {start} and {end}: {random_number}")
