for a in range(1,1000):
	for b in range(a, 1000 - a):
		c = 1000 - a - b

		if c<b:
			break
		if (a ** 2 + b ** 2 == c ** 2):
			print(a,b,c)
			print("Product: ", a*b*c)
