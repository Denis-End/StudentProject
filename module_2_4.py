numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    #print(i)
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            is_prime == False
            break
        if is_prime == True:
            primes.append(i)
            break

print(not_primes)
print(primes)