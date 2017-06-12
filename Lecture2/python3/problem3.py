def gen_prime(n):
    primes = [2]
    if n == 1:
        yield primes[0]
    else:
        yield primes[0]
        for x in range(n-1):
            potential_prime = primes[-1]
            if potential_prime == 2:
                potential_prime += 1
            else:
                potential_prime += 2
            while True:
                res = map(lambda x: potential_prime % x, primes)
                if all(res):
                    primes.append(potential_prime)
                    yield primes[-1]
                    break
                potential_prime += 2
            
how_many = int(input("How many primes: "))
for prime in gen_prime(how_many):
    print(prime)