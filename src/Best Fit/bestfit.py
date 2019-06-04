import argparse
import operator
import os
import sys
import time

from argparse import ArgumentParser
from random import randint
from Bin import Bin


def pack(values, capacity):
    values = sorted(values, reverse=True)
    bins = []

    for item in values:
        bestfit = capacity
        best_bin = -1
        i = 0
        # Try to fit item into a bin
        while i < len(bins):
            if ((capacity - (bins[i].sum + item)) < bestfit) and (bins[i].sum + item <= capacity):
                bestfit = capacity - (bins[i].sum + item)
                best_bin = i
            i += 1
        if best_bin != -1:
            bins[best_bin].sum += item
            bins[best_bin].items.append(item)
        else:
            b = Bin()
            b.capacity = capacity
            b.sum += item
            b.items.append(item)
            bins.append(b)
            

    return bins

def return_fitness(capacity, bins):
    fitness = 0
    for i in range(len(bins)):
        fitness += ((bins[i].sum / capacity) ** int(2)) / len(bins)

    return fitness


def Main_driver():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="Must have a data file for input")
    parser.add_argument("-c", "--capacity", required=True, help="Must have a maximum bin capacity")
    args = parser.parse_args()

    capacity = int(args.capacity)

    INPUT_FILE = args.file
    start = time.time()
    data_file = open(INPUT_FILE, 'rt')
    read_in_data_file = []
    for value in data_file.read().split():
        read_in_data_file.append(int(value))

    bins = pack(read_in_data_file, capacity)

    fitness = return_fitness(capacity, bins)

    end = time.time()
    alg_time = end - start
    
    print("Best Fit bin count: [" + str(len(bins)) + "]\n")
    print("Best Fit fitness: [" + str(fitness) + "]\n")
    print("The Best Fit Algorithm took [" + str(alg_time) + "] seconds.\n")

Main_driver()