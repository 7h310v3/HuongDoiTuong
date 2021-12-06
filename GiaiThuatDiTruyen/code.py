import random
from deap import base, creator, tools

def eval_func(individual):
   target_sum = 15
   return len(individual) - abs(sum(individual) - target_sum),