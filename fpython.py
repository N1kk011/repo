import random

def generate_lottery_numbers():
    main_numbers = random.sample(range(1, 70), 5)  # Generate 5 unique numbers between 1 and 69
    powerball = random.randint(1, 26)  # Generate a Mainball number between 1 and 26
    main_numbers.sort()  # Sort the main numbers in ascending order
    return main_numbers, powerball

# Example usage
main_numbers, powerball = generate_lottery_numbers()

print(f"Today's lottery numbers are: {main_numbers} and the Mainball is: {powerball}")
