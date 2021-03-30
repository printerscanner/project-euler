import time, math

start = time.time()

def isPrime(n):
	if (n+1)%6 == 0 or (n-1)%6 == 0:
		for i in range(2,int(round(math.sqrt(n)+1))):
			if n%i == 0:
				return False
		return True
	return False

counter = 2
i = 4

prime = 0

while counter < 10001:
	if isPrime(i):
		counter = counter + 1
		prime = i
		i = i + 1
	i = i + 1

print str(counter)+ " prime is "+ str(prime)

end = time.time()

print end-start