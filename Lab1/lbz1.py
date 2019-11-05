dataset = [[0,0,0],
			[0,0,1],
			[0,1,0],
			[0,1,1],
			[1,0,0],
			[1,0,1],
			[1,1,0],
			[1,1,1]]; #вхідні дані

weight = [0.57, 0.17, 0.73] #вагові коефіцієнти
tresshold = .5 #порогове значення
runCycle = True #Запуск циклу
stepsCounter = 0 #Лічильник кроків
n = .05 #Коефіцієнт швидкости навчаннє

logic_fun = lambda x1,x2,x3: (not(x1) or x2) and x3
perceptron = lambda x,w: 1 if x[0]*w[0] + x[1]*w[1] + x[2]*w[2] > tresshold else 0

while runCycle and stepsCounter < 100:
	runCycle = False
	for i in dataset:
		teacher = logic_fun(i[0],i[1],i[2])
		student = perceptron(i,weight)
		print("Вчитель: " + str(teacher) + "\tУчень: " + str(student))
		if(teacher != student):
			for j in range(3):
				weight[j] += n*i[j]*(teacher - student)
			runCycle = True

	stepsCounter += 1

	print("Крок: " + str(stepsCounter) + "\n")
print("Кількість кроків: " + str(stepsCounter))