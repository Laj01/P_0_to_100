import sys


def main():
    try:
        user_input = int(input('Enter an integer: '))
        prime_checker(user_input)
    except:
        sys.exit('Invalid number!')

def prime_checker(number):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f'The number {number} is a prime.')
    else:
        print(f'The number {number} is NOT a prime.')


if __name__ == '__main__':
    main()