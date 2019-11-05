import random

#Crossing function
def crossing(parrent,partner,crossing_line):
	parrent2 = parrent.copy()
	parrent2[crossing_line:len(parrent2)] = partner[crossing_line:len(partner)]
	return parrent2

#Mutation function
def mutation(arr,index):
	arr[index] = "0" if arr[index] == "1" else "1"
	return arr

#Rullet function
def rullet(popArr, gfvArr, n):
	rulletRezult = []
	run = True
	while run:
		run = False
		differenceArr = []
		r = random.random()
		#print("random: " + str(r))
		#print("sum: " + str(sum(gfvArr)))
		if len(rulletRezult) != n:
			for i in range(0, n):
				rating = gfvArr[i]/sum(gfvArr)
				#print("rating: " + str(rating)
				#print(abs(rating - r))
				differenceArr.append(abs(rating - r))
			minIndex = differenceArr.index(min(differenceArr))
			#print("minIndex: " + str(minIndex))
			rulletRezult.append(popArr[minIndex])
			run = True
			
	return rulletRezult
	#print(rulletRezult)