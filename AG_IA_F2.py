#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import math


# TAM_POP: tamanho das dimensões (recomendável n = 30)
TAM_POP = 30
# Intervalo -100 a 100
TAM_CROMO = 8

def print_pop(pop):
	for ind in pop:
		print('\t' + ''.join(str(e) for e in ind) + "\t=> " +str(bin_to_int(ind)))

# Manutenção        
def gen_pop():
	pop = []
	for i in range(TAM_POP):
		cromo = [1, 1, 1, 1, 1, 1, 1, 1]
		while (bin_to_int(cromo) > 100 or bin_to_int(cromo) < -100):
			cromo = []            
			for j in range(TAM_CROMO):
				cromo.append(random.choice([0, 1]))
		pop.append(cromo)
	return pop

def bin_to_int(ind):
	genes = ''.join(str(e) for e in ind)
	value = int(genes[1:], 2)
	value = (value * -1) if ind[0] == 1 else value 
	return value

def fitness(cromo=None):
	int_ = bin_to_int(cromo)    
	return (int_) if int_ > 0 else int_ * -1

def best_fitness(pop):
	somatorio = 0
	produto = 1
	for cromo in pop:
		f = fitness(cromo)
		somatorio += f
		produto *= f 
	print('somatorio + produto: {}\n'.format(somatorio + produto))
	return somatorio + produto

def mutacao(pop):
	a = random.choice(range(TAM_POP))
	b = random.choice(range(TAM_CROMO))    
	if fitness(pop[a]) != 0:
		pop[a][b] = 1 - pop[a][b]
		cromo = pop[a]
		if (bin_to_int(cromo) > 100 or bin_to_int(cromo) < -100):
			pop[a][b] = 1 - pop[a][b]
	return pop

def cruzamento(pop):
	pop1 = pop
	a = random.choice(range(TAM_POP))
	lutador = pop.pop(a)
	b = random.choice(range(TAM_POP-1))
	lutador2 = pop.pop(b)
	
	pai = None
	if fitness(lutador) < fitness(lutador2):
		pop.append(lutador2)
		pai = lutador
	else:
		pop.append(lutador)
		pai = lutador2

	a = random.choice(range(TAM_POP-1))
	lutador3 = pop.pop(a)
	b = random.choice(range(TAM_POP-2))
	lutador4 = pop.pop(b)
	if fitness(lutador3) < fitness(lutador4):
		pop.append(lutador4)
		mae = lutador3
	else:
		pop.append(lutador3)
		mae = lutador4

	metade = int((TAM_CROMO/2) + 1)   
    
	if fitness(mae) != 0 and fitness(pai) != 0:
        # cruzando
		filho = pai[0:metade] + mae[metade:TAM_CROMO]
		filho2 = mae[0:metade] + pai[metade:TAM_CROMO]
		if (bin_to_int(filho) > 100 or bin_to_int(filho) < -100 or bin_to_int(filho2) > 100 or bin_to_int(filho2) < -100):
			pop.append(mae)
			pop.append(pai)
			pop = cruzamento(pop)
		else:
			pop.append(filho)
			pop.append(filho2)            
	else:
		pop.append(mae)
		pop.append(pai)
        
	return pop

if __name__ == '__main__':
	k = 1
	populacao = gen_pop()
	print('Geração: {}'.format(k))
	print_pop(populacao)               
	f = best_fitness(populacao)
	while(f != 0):
		k += 1
		cruzamento(populacao)
		mutacao(populacao)
		print('Geração: {}'.format(k))        
		print_pop(populacao)        
		f = best_fitness(populacao)


# In[ ]:




