num = eval(input("请输入学生人数:\n"))
i = 1
best = 0
while i <= num:
	a = eval(input("请输入第" + str(i) + "位学生的成绩:\n"))
	if a >= best:
		best = a
	i += 1
print(best)