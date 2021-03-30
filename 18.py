#http://radiusofcircle.blogspot.com

#importing time module
import time

#time at the start of execution
start = time.time()

#numbers copied as string
number = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

#splitting the number into a list
number = number.strip().split('\n')

#converting each and every list of strings to int
for i in xrange(1,len(number)):
	number[i] = number[i].strip().split(' ')
	number[i] = [int(x) for x in number[i]]

#adding the first number bcz we could not do the above
#operation as this one one number
number[0] = [75]

#counter for counting number of iterations
counter = 0

#for loop for bottom-up approach
for i in xrange(len(number)-2,-1,-1):
	for j in xrange(len(number[i])):
		number[i][j] = number[i][j] + max(number[i+1][j], number[i+1][j+1])
		counter += 1
	number.pop()

#printing the output
print 'Found {} in {} iterations'.format(number[0][0],counter)

#time at the end of execution
end = time.time()

#printing the total time
print end-start