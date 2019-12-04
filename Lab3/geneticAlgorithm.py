import random
import grayAndBinConvertor as gbc
import geneticOperations as gen_ops

class GeneticAlgorithm:
	def __init__(self, n, steps, p_crossing, p_mutation, search_val):
		self.n = n
		self.steps = steps
		self.p_crossing = p_crossing
		self.p_mutation = p_mutation
		self.search_val = search_val

	def crossing(self, pop):
		print("Схрещування")
		cross_index = random.randint(0,(self.n-1))
		pop_cross = []
		for i_cross in range(self.n):
			if cross_index == pop[i_cross]:
				cross_index = random.randint(0,(self.n-1))
			cross_line = random.randint(0,(self.n-1))
			pop_cross.append(gen_ops.crossing(pop[i_cross],pop[cross_index],cross_line))
				
		pop = pop_cross

	def mutation(self, pop):
		print("Мутація")
		index = random.randint(0,(self.n-1))
		pop[index] = gen_ops.mutation(pop[index],index)

	def run(self):
		pop = [] #Populations (binary val of fenotype) list
		fen_arr = [] #Fenotypes list
		gfv_arr = [] #Goal function values list
		run_cycle = True #Run Cycle
		steps_counter = 0 #Steps Counter

		#Goal Function
		goal_fun = lambda x: round(x**6 - x**4 + (x**6 - x**4)**.5)

		#Write data into lists
		for x in range(self.n):
			r = random.randint(-50,50)
			fen = r if r != 0 else random.randint(-50,50) #fenotype
			fen_arr.append(fen)
			gfv_arr.append(goal_fun(fen))
			pop.append(gbc.bin_to_gray(gbc.dec_to_bin(fen)))

		best_fen = fen_arr[fen_arr.index(max(fen_arr))] #Best fenotype
		print(fen_arr)
		print("Топ: " + str(best_fen))
		for p in pop:
			print(p)
		print("\n")

		live = 0
		
		while(run_cycle and steps_counter < self.steps):
			steps_counter += 1

			for i_s in range(self.n):
				if gfv_arr[i_s] > self.search_val:
					print("Шукане значення знайдено")
					run_cycle = False
					break

			if live > 15:
				run_cycle = False

			#Вибірка
			pop = gen_ops.rullet(pop,gfv_arr,self.n)

			#Схрещування або мутація
			rand_val = random.random()
			if((rand_val <= self.p_crossing) and (rand_val > self.p_mutation)):
				self.crossing(pop)
			elif rand_val <= self.p_mutation:
				self.mutation(pop)

			#Оновлення значень для оцінки
			fen_arr = []
			gfv_arr = []

			for j_push in range(self.n):
				fen = gbc.bin_to_dec(gbc.gray_to_bin(pop[j_push]))
				fen_arr.append(fen)
				gfv_arr.append(goal_fun(fen))

			for i_live in range(self.n):
				if best_fen == fen_arr[i_live]:
					live += 1
					break
				elif((best_fen != fen_arr[i_live]) and (i_live == len(fen_arr) - 1)):
					live = 0
					best_fen = fen_arr[fen_arr.index(max(fen_arr))]
					print("Новий топ: " + str(best_fen))
				
			print(fen_arr)
			for p in pop:
				print(p)
			print("\n")

		print("Скільки поколінь вижив топ ("+str(best_fen)+"): " + str(live))
		print("Кількість ітерацій: " + str(steps_counter))