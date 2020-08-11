def sum_of_primes(n):
    is_prime = set(range(3, n+1, 2))
    #create set excluding even numbers
    for i in range(3, int(n**0.5) + 1):
        if i not in is_prime:
            #number has a prime factor
            continue
        possible_prime = i
        while possible_prime < n:
            possible_prime += i
            if possible_prime in is_prime:
                #remove multiples of prime found
                is_prime.remove(possible_prime)
    sum_prime = 2+ sum(is_prime)
    print(sum_prime)
