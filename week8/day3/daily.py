import random


class DNA():

    def __init__(self):
        self.dna = []

    def make_genome(self):
        index = 0
        while (index < 10):
            chromosome = Chromosome()
            chromosome = chromosome.define_chromosome()
            self.dna.append(chromosome)
            index += 1
        print(len(self.dna))

    def display_genome(self):
        print(self.dna)


class Chromosome():

    def __init__(self):
        self.chromosome = []

    def define_chromosome(self):
        index = 0         #is this acceptable to do in python, or is is there a pythonic way to do it?
        while (index < 10):
            self.chromosome.append(random.randint(0,1))
            index += 1
        return self.chromosome



organism = DNA()
my_chromosome = Chromosome()
organism.make_genome()

# organism.make_genome()
# print(organism.make_genome())