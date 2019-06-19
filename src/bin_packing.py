import argparse
import operator
import os
import sys
import time
import math
import numpy

from argparse import ArgumentParser
from numpy.random import choice
from chromosome import chromosome
from Bin import Bin
import random


CHROMOSOME_LENGTH	= 0
CURRENT_GENERATE	= 0
ELITISM				= float(0.0)
INPUT_FILE			= ''
MUTATION_RATE		= float(0.0)

CURR_POP		= []
NEXT_POP		= []

parser = ArgumentParser()
numpy.random.RandomState(seed=None)
parser.add_argument("-f", "--file", required=True, help="Must have a data file for input")
parser.add_argument("-m", "--mutation", required=False, type=float, default=.10)
parser.add_argument("-p", "--pop_size", required=False, type=int, default=10)
parser.add_argument("-g", "--generation_size", required=False, type=int, default=5000)
parser.add_argument("-c", "--capacity", required=False, type=int, default=100)
parser.add_argument("-k", "--constant", required=False, type=int, default=2)
parser.add_argument("-d", "--debug", required=False, type=bool, default=False)
parser.add_argument("-s", "--survial", required=False, type=int, default=4)
parser.add_argument("-o", "--output_file", required=False, type=str, default=time.time())

args = parser.parse_args()

sys.stdout = open(".\\" + str(args.output_file) + ".txt", 'wt')
INPUT_FILE        = args.file
MUTATION_RATE    = args.mutation
POP_SIZE        = args.pop_size
CAPACITY        = args.capacity
GEN_SIZE        = args.generation_size
DEBUG            = args.debug
CONSTANT         = args.constant
SURVIAL            = args.survial

def mutation(mutate_me):

	removed_bins = []
	removed_bin_index = []
	flat_list = []
	probabilities = [MUTATION_RATE, 1 - MUTATION_RATE]

	for i in range(len(mutate_me.bins)):
		delete_bin = choice([True, False], p=probabilities)
		if(delete_bin):
			removed_bins.append(mutate_me.bins[i].items)
			removed_bin_index.append(i)

	removed_bin_index.reverse()
	for j in removed_bin_index:
		mutate_me.bins.pop(j)

	for sublist in removed_bins:
		for item in sublist:
			flat_list.append(item)

	mutate_me.best_pack_bins(flat_list, CAPACITY)
	mutate_me.set_fitness(CONSTANT, CAPACITY)

	return mutate_me

def selection():
	competitors = random.sample(CURR_POP, SURVIAL)

	for home_opponent in competitors:

		for away_opponent in competitors:
			if away_opponent.fitness == home_opponent.fitness:
				break
			elif away_opponent.fitness > home_opponent.fitness:
				away_opponent.rank += 1
			else:
				home_opponent.rank += 1

	competitors.sort(key=operator.attrgetter('rank'))
	for x in range(len(competitors)):
		competitors[x].rank = 0
	# return the best chromosome from the sample set
	return competitors[0]


def Main_driver():

	# vars
	global CURR_POP
	global NEXT_POP
	global CURRENT_GENERATE

	data_file = open(INPUT_FILE, 'rt')
	read_in_data_file = []
	for value in data_file.read().split():
			read_in_data_file.append(value)

	# init the first generate population at random
	for x in range(POP_SIZE):
		CURR_POP.append(chromosome(CAPACITY))
		shuffled_data = read_in_data_file.copy()
		random.shuffle(shuffled_data)
		CURR_POP[x].worst_pack_bins(shuffled_data, CAPACITY)
		CURR_POP[x].set_fitness(CONSTANT, CAPACITY)

	start_time = time.time()
	Generation = 0
	if(DEBUG):
		print("---DEBUG MODE ACTIVATED---")
		print("-----------------------------------------------------------------------------------")
	else:
		print("Current Generation |Worst Fitness  |Mean Fitness  |Best Fitness   |Lowest Bin Count")

	while(CURR_POP[0].fitness != 1 and Generation <= GEN_SIZE):
		Generation += 1
		the_lucky_one = chromosome(CAPACITY)
		the_lucky_one = selection()


		mutation(the_lucky_one)

		if(the_lucky_one.fitness > (sum(curr.fitness for curr in CURR_POP) / len(CURR_POP)) ):
			CURR_POP.sort(key=operator.attrgetter('fitness'), reverse=True)
			dead_chr = CURR_POP.pop()
			CURR_POP.append(the_lucky_one)

		if(DEBUG):
			CURR_POP.sort(key=operator.attrgetter('fitness'), reverse=True)
			print("--------------------Generation [%d]--------------------" % Generation)
			print("Chromosome number | Fitness | Bin Count")

			for b in range(len(CURR_POP)):
				print("%-18d| %-8f| %-10d" %(b, CURR_POP[b].fitness, len(CURR_POP[b].bins)))
		else:
			CURR_POP.sort(key=operator.attrgetter('fitness'), reverse=True)
			mean_fitness = sum(curr.fitness for curr in CURR_POP) / len(CURR_POP)
			print("%-19i|%-15f|%-14f|%-15f|%-17i" %
				     ( Generation, CURR_POP[-1].fitness, mean_fitness, CURR_POP[0].fitness, len(CURR_POP[0].bins)))


	print('-' * 30)

	print("--- %s seconds ---" % (time.time() - start_time))



Main_driver()