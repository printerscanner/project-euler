
import math


def find_divisors(number):
	total = 0
	for i in range(1,int(math.ceil(math.sqrt(number)))):
		if number % i == 0:
			total+=1
	return total

# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes

def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
    	if prime[p] == False:
    		if find_divisors(p) > 500:
    			print(p)

        # if prime[p]:
        #     print p, #Use print(p) for python 3



print(SieveOfEratosthenes(100000000))

# I also used the same method as euler with the following optimization.
# 1.starting with an even (n) generate prime factors of (n/2). save as groupn
# 2. generate prime factors of (n+1). save as groupn+1.
# 3. Combine the prime factors and then caclculate divisors.
# 4. if not solution increment test value of n by 2.
# 5. generate factors of n/2.--> group n
# 6. combine factors.
# 7. if not solution generate factors of n+1.--> groupn+1
# 8. combine.
# 5. if not solution increment n by 2. goto step2.

# Optimization is achieved by factoring smaller numbers which take lot less time and reusing previously generated factors.
