#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random
import math

TAM_POP = 6

def print_pop(pop):
	print('Population:')
	for ind in pop:
		print('\t' + ''.join(str(e) for e in ind) + "\t=> " +str(bin_to_int(ind)))

def gen_pop():
	pop = []
	for i in range(TAM_POP):
		cromo = []
		for j in range(6):
			cromo.append(random.choice([0, 1]))
		pop.append(cromo)
	return pop

def bin_to_int(ind):
	genes = ''.join(str(e) for e in ind)
	value = int(genes[1:], 2)
	value = (value * -1) if genes[0] == '1' else value 
	return value

def fitness(cromo=None):
	int_ = bin_to_int(cromo)
	return int(math.pow(int_, 2))

def best_fitness(pop):
	best = 99999
	for cromo in pop:
		f = fitness(cromo)
		if f < best:
			best = f
	return best

def mutacao(pop):
	a = random.choice(range(6))
	m = pop.pop(a)
	m[a] = 1 - m[a]
	pop.append(m)
	return pop

def cruzamento(pop):
	a = random.choice(range(6))
	lutador = pop.pop(a)
	b = random.choice(range(5))
	lutador2 = pop.pop(b)
	
	pai = None
	if fitness(lutador) < fitness(lutador2):
		 pop.append(lutador2)
		 pai = lutador
	else:
		pop.append(lutador)
		pai = lutador2


	a = random.choice(range(5))
	lutador3 = pop.pop(a)
	b = random.choice(range(4))
	lutador4 = pop.pop(b)
	if fitness(lutador3) < fitness(lutador4):
		 pop.append(lutador4)
		 mae = lutador3
	else:
		pop.append(lutador3)
		mae = lutador4
        
	# cruzando
	filho = pai[0:3] + mae[3:]
	filho2 = mae[0:3] + pai[3:]
	pop.append(filho)
	pop.append(filho2)
	return pop

if __name__ == '__main__':
	populacao = gen_pop()
	best = 99999
	k = 0
	while(best != 0):
		k += 1
		print('geracao: {}'.format(k))
		print_pop(populacao)
		f = best_fitness(populacao)
		if f < best:
			best = f
			if best == 0:
				print('FIM!')
				break
		cruzamento(populacao)
		mutacao(populacao)		

