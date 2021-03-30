def collatz_sequence(n):
	chain_length = 1
	while n > 1:
		if n % 2 ==0:
			n = n/2
		else:
			n = 3*n + 1
		chain_length+=1
	return chain_length

start = 1
MaxCount = 1
for i in range(1,1000000):
	count = collatz_sequence(i)
	if count >= MaxCount:
		MaxCount = count
		start = i
print(MaxCount, start)

