#!/usr/bin/env python
# coding: utf-8

# In[2]:


# https://www.youtube.com/watch?v=uQj5UNhCPuo

from collections import namedtuple
from functools import partial
import random


# In[3]:


Thing = namedtuple('Thing', ['name', 'value', 'weight'])

first_example = [
    Thing('Laptop', 500, 2200),
    Thing('Headphones', 150, 160),
    Thing('Coffee Mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water Bottle', 30, 192),
]

second_example = [
     Thing('Mints', 5, 25),
     Thing('Socks', 10, 38),
     Thing('Tissues', 15, 80),
     Thing('Phone', 500, 200),
     Thing('Baseball Cap', 100, 70)
 ] + first_example


# In[4]:


def generatePopulation(size, lengthOfGenome):
    return [random.choices([0, 1], k=lengthOfGenome) for _ in range(size)]

def fitness(genome, things, weightLimit):
    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value
        if weight > weightLimit:
            return 0 # combination of things cannot exceed the limit
    return value

def crossover(genome1, genome2):
    p = random.randint(1, len(genome1)-1)
    return genome1[0:p]+genome2[p:], genome2[0:p]+genome1[p:]

def mutation(genome, num=1, prob=0.5):
    for _ in range(num):
        if random.random() <= prob:
            randIdx = random.randrange(0, len(genome), 1)
            genome[randIdx] = 1-genome[randIdx]
    return genome

def selection(population, fitnessFunc):
    return random.choices(population, weights=[fitnessFunc(p) for p in population], k=2)

def genomeToString(genome, things):
    result = []
    for i, g in enumerate(genome):
        if g==1:
            result.append(things[i].name)
    return result


# In[5]:


def evolution(populationSize, generationLimit, items, fitnessFunc):
    population = generatePopulation(populationSize, lengthOfGenome=len(items)) # random initialization

    for i in range(generationLimit):
        bestIndividual = sorted(population, key=lambda genome: fitnessFunc(genome), reverse=True)[0]
        # the individual already has good enough performance
        if fitnessFunc(bestIndividual) >= fitnessLimit:
            return bestIndividual, i
        else:
            next_gen = []
            for j in range(int(len(population)/2)):
                parents = selection(population, fitnessFunc)
                offspring1, offspring2 = crossover(parents[0], parents[1])
                offspring1 = mutation(offspring1)
                offspring2 = mutation(offspring2)
                next_gen.append(offspring1)
                next_gen.append(offspring2)
            population = next_gen

    return 'Result not found', -1


# In[7]:


populationSize = 10
generationLimit = 100
items = second_example
if len(items) == 5:
    fitnessLimit = 740 # 740: laptop, headphones, coffee mug, water bottle
else:
    fitnessLimit = 1310
    # 1310: laptop, headphones, coffee mug, baseball cap, phone OR
    #       mints, socks, tissues, phone, baseball cap, laptop, headphones, water bottle
fitnessFunc = partial(fitness, things=items, weightLimit=3000)

genomeResult, i = evolution(populationSize, generationLimit, items, fitnessFunc)
solution = genomeToString(genomeResult, items)
print('Found solution is:', solution)
print(f'Result fitness is {fitnessFunc(genomeResult)}')
print(f'It takes genetic algorithm {i} generations to find the solution')

