power = 2**1000

arr = map(int, str(power))
total = 0
for i in range(0,len(arr)):
	total+=arr[i]
print(total)

