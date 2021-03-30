# counter = 0
# for i in range(1901,2001):
# 	if i%400==0 :
# 		counter+=366
# 	elif i%4==0 and i%100 !=0:
# 		counter+=366
# 	else:
# 		counter+=365

# print counter

# january = 1
# february = 31
# march = 59 or 60
# april = 90 or 91
# may = 120 or 121
# june = 151 or 152
# july = 181 or 182
# august = 212 or 213
# september = 243 or 244
# october = 273 or 274
# november = 303 or 304
# december = 334 or 335



# counter = 0
# for i in range(1901, 2001):
# 	for j in range(1,366):
# 		if (i%4==0 and i%100!=0) or (i%400==0):
# 			if j==1 or j==32 or j==61 or j==92 or j==122 or j==153 or j==183 or j==214 or j==245 or j==275 or j==305 or j==336 and j%7==0:
# 				counter+=1
# 			elif j==1 or j==32 or j==60 or j==91 or j==121 or j==152 or j==182 or j==213 or j==244 or j==274 or j==304 or j==335 and j%7==0:
# 				counter+=1

# print counter

# from datetime import date
# from collections import Counter

# counter = Counter()

# for year in xrange(1901, 2001):
#     for month in xrange(1, 13):
#         day = date(year, month, 1)
#         counter[day.weekday()] += 1

# print counter[6]

months = { 1: 31,
        2 : 28,
       3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31}

day = 1
sundays = 0

for i in xrange(1901,2001):
	for m in months:
		 day += months[m]
            if year % 4 == 0 and m == 2:
                day += 1
            if day % 7 == 0:
                sunday_count += 1

print "Sundays:", sunday_count