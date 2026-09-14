from prime_square_data import squares_generator , primes_generator
even=set(range(0,50,2))
odd=set(range(1,50,2))
print(even)
print(odd)
primes=set(primes_generator(100))
print(primes)

sqaures=set(squares_generator(100))
print(sqaures)

print(odd.difference(primes))

print(odd-primes)