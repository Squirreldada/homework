best = 100
for i in range(1,6,1):
	time = eval(input("请输入第"+str(i)+"位同学的短跑测试时间："))
	if time < best:
		best = time
print(best)