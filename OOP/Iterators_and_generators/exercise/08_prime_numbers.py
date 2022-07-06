def get_primes(num_list):
    for num in num_list:
        is_prime = True
        for n in range(2, num):
            if num % n == 0:
                is_prime = False
                break
        if num > 1 and is_prime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([-2, 0, 0, 1, 1, 0])))