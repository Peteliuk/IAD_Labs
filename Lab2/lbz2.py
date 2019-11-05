data = [[0,1,0,0,0,0,0,0,1], #Кузь
		[0,1,0,1,0,0,0,0,1],
		[0,1,0,0,0,0,0,1,1],

		[0,1,0,1,0,1,0,0,0], #Микола
		[0,1,1,1,0,1,0,0,0],
		[0,1,0,1,1,1,0,0,0],

		[1,1,0,0,0,1,0,1,0],
		[1,1,0,0,1,1,0,1,0],
		[1,1,0,0,0,1,1,1,0]] #Батькович

w_old = [[.09,.12,.32,.31,.45,.92,.56,.04,.81],
         [.39,.34,.67,.08,.35,.22,.76,.64,.01],
         [.58,.68,.75,.14,.18,.14,.24,.43,.57]]

w_new = [[.09,.12,.32,.31,.45,.92,.56,.04,.81],
         [.39,.34,.67,.08,.35,.22,.76,.64,.01],
         [.58,.68,.75,.14,.18,.14,.24,.43,.57]]

n = .6 #Коефіцієнт швидкості навчання
k = .5 #коефіцієнт оновлення для n
tresshold = .0005 #Порогове значення

steps = 0 
runCycle = True
distance_array = []

def distance(x,w):
	sumator = 0
	for i in range(len(data[0])):
		sumator += (w[i] - x[i])**2
	return sumator

while runCycle and steps < 100:
	runCycle = False

	for i in data:
		a1 = distance(i, w_new[0])
		a2 = distance(i, w_new[1])
		a3 = distance(i, w_new[2])
		distance_array.append([a1,a2,a3])
		for j in range(len(w_new[0])):
			if a1 < a2 and a1 < a3:
				#print("Winner A1")
				w_old[0][j] += n*(i[j] - w_old[0][j])
				w_new[0][j] = w_old[0][j] + n*(i[j] - w_old[0][j])
			elif a2 < a1 and a2 < a3:
				#print("Winner A2")
				w_old[1][j] += n*(i[j] - w_old[1][j])
				w_new[1][j] = w_old[1][j] + n*(i[j] - w_old[1][j])
			elif a3 < a2 and a3 < a1:
				#print("Winner A3")
				w_old[2][j] += n*(i[j] - w_old[2][j])
				w_new[2][j] = w_old[2][j] + n*(i[j] - w_old[2][j])
	steps += 1
	n *= k

	'''**************** Stop Condition ************************'''
	for i_stop in range(len(w_new)):
		for j_stop in range(len(w_new[0])):
			if(abs(w_new[i_stop][j_stop] - w_old[i_stop][j_stop]) > tresshold):
				runCycle = True


for i in range(len(data)):
	print(str(data[i]) + "\tКлас: " + str(distance_array[i].index(min(distance_array[i]))+1))
print("Кількість кроків: " + str(steps))