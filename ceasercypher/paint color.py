import math


def calculate(height, width, coverage):
    num_cans = (height*width)/coverage
    round_up_cans = math.ceil(num_cans)
    return round_up_cans


user_height = int(input('Enter the height: '))
user_width = int(input('Enter the width: '))
user_coverage = int(input('Enter the coverage: '))
calculation = calculate(user_height, user_width, user_coverage)
print(f'the required paints for the surface is {calculation}')