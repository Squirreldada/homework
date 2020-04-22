num = eval(input("请输入总人数："))
sum = 0
for i in range(0,num,1):
	sum += eval(input("请输入第"+str(i+1)+"个人的竞赛成绩："))
print(sum/num)