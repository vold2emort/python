def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f'The number {num} is prime')
    else:
        print(f'The number {num} is not prime')


user_number = int(input('Enter the number: '))
prime_checker(user_number)
