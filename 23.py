def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n

count = 0
for i in range(0, 28123):
	if is_abundant(i) is False:
		count += i
		print count
print count