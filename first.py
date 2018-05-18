#统计每个字符串的个数 如果是空格则不统计，打印出现闪数前10的字符
#Modify

content = 'first of all,i want make it clear that i can not claim understanding this holy book in just'
res = {}
for s in content:
	if s == ' ':
		continue
	if s not in res:
		res[s] = 1
	res[s] += 1
res_list = []
for k in res.keys():
	res_list.append([k,res[k]])
for i in range(10):
	for j in range(len(res_list) - 1 -i):
		if res_list[j][1] > res_list[j+1][1]:
			res_list[j],res_list[j+1] = res_list[j+1],res_list[j]
for r in res_list[-10:]:
	print 'char %s count is %s' % (r[0],r[1])
