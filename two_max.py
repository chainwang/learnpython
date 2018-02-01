
lst = [1,2,3,2,12,3,13,21,2333,244,65555,1000,209,65555]
first_max = 0 
second_max = 0
for num in lst:
	if num > first_max:
		second_max = first_max
		first_max = num
	elif num > second_max:
		second_max = num
print 'first_max = %s' % first_max
print 'second_max = %s' % second_max
 
