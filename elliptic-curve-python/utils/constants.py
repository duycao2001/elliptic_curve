from utils.int_operations import is_prime
PRIME_NUMBERS_2_TO_4_DIGITS = list(filter(lambda num: is_prime(num), [
    i for i in range(10, 10000)]))
