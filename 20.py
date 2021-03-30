counter = 1

for i in xrange(100,0,-1):
	counter = counter*i
print counter

counter = [int(i) for i in str(counter)]

sum_counter = 0
for i in range(0, len(counter)):
	sum_counter+=counter[i]
print sum_counter