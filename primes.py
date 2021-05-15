def primes_rows(up_to_number):
    row = [1, 5, 7, 11]
    primes = []
    isPrime = False

    while row[0] < up_to_number:
        for x in range(len(row)):
            current_number = row[x]

            # check if current_number is on not-prime list
            for prime in primes:
                if current_number == prime[1][x]:
                    isPrime = False
                    # update not-prime
                    prime[1][x] += prime[0] * 12

            # add prime number and its not-prime list
            if isPrime:
                sqaure = current_number ** 2
                if x == 1 or x == 3:
                    primes.append([ current_number, [sqaure, sqaure + current_number * 8, sqaure + current_number * 6, sqaure + current_number * 2] ])
                else:
                    primes.append([ current_number, [sqaure, sqaure + current_number * 4, sqaure + current_number * 6, sqaure + current_number * 10] ])

            row[x] += 12
            isPrime = True

    for prime in primes:
        print(prime)


primes_rows(1020)
