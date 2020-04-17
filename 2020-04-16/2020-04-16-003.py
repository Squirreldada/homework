best_score = 0
best_num = 0
i = 1
a = 0
while i <= 10:
	a = eval(input("请输入第" + str(i) + "名同学的成绩"))
	if a >= best_score:
		best_score = a
		best_num = i
	i += 1
print("已接收10位学生的成绩\n成绩最好的是第" + str(best_num) + "位同学\n成绩为:" + str(best_score))