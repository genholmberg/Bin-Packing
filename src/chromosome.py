from random import randint
from Bin import Bin

class chromosome:
	def __init__(self, capacity):
		self.fitness 	= 0
		self.rank		= 0
		self.bins		= []
		temp = Bin()
		temp.capacity = capacity
		self.bins.append(temp)

	def set_fitness(self, k, capacity):
		self.fitness = 0
		for i in range(len(self.bins)):
			self.fitness += ( (self.bins[i].sum / capacity) ** k) / len(self.bins)

	def best_pack_bins(self, data_array, capacity):

		capacity = int(capacity)

		for item in data_array:
			item = int(item)
			bestfit = capacity
			best_bin = -1
			i = 0
			# Try to fit item into a bin
			while i < len(self.bins):
				if ((capacity - (self.bins[i].sum + item)) < bestfit) and (self.bins[i].sum + item <= capacity):
					bestfit = capacity - (self.bins[i].sum + item)
					best_bin = i
				i += 1
			if best_bin != -1:
				self.bins[best_bin].sum += item
				self.bins[best_bin].items.append(item)
			else:
				b = Bin()
				b.capacity = capacity
				b.sum += item
				b.items.append(item)
				self.bins.append(b)

	def worst_pack_bins(self, data_array, capacity):

		capacity = int(capacity)

		for item in data_array:
			item = int(item)
			worstfit = capacity
			worst_bin = -1
			i = 0
			# Try to fit item into a bin
			while i < len(self.bins):
				if ((capacity - (self.bins[i].sum + item)) > worstfit) and (self.bins[i].sum + item <= capacity):
					worstfit = capacity - (self.bins[i].sum + item)
					worst_bin = i
				i += 1
			if worst_bin != -1:
				self.bins[worst_bin].sum += item
				self.bins[worst_bin].items.append(item)
			else:
				b = Bin()
				b.capacity = capacity
				b.sum += item
				b.items.append(item)
				self.bins.append(b)
