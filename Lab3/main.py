from geneticAlgorithm import GeneticAlgorithm

n = 4 #Number of chromosomus
steps = 100 #Needed number of steps
p_crossing = .7 #Crossing posibility
p_mutation = .1 #Mutation posibility
search_val = 9996680000000 #Searching number

gen_alg = GeneticAlgorithm(n,steps,p_crossing,p_mutation,search_val)
gen_alg.run()