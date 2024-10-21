import numpy as np
from layer import Layer

class FC:

	def __init__(self, input_size, output_size):
		self.weights = np.random.rand(input_size, output_size) - 0.5
		self.biases = np.random.rand(1, output_size) - 0.5


	def forward(self, input_data):
		self.input = input_data
		Z = np.matmul(self.input, self.weights) + self.biases
		return self.output

	def backward(self, )
