import random


class Gene:

    def __init__(self):
        self.gene = random.randint(0, 1)

    def mutate(self):
        if self.gene == 0:
            self.gene = 1
        else:
            self.gene = 0
        return self.gene

    def __str__(self):
        return f"{self.gene}"

    def __repr__(self):
        return f"{self.gene}"


class Chromosome:

    def __init__(self):
        self.chromosome = [Gene() for i in range(10)]

    def gene_to_mutate(self):
        pass

    def __str__(self):
        return f"{self.chromosome}"

    def __repr__(self):
            return f'{self.chromosome}'


class DNA:

    def __init__(self):
        self.dna = [Chromosome() for i in range(10)]

    def chromosome_to_mutate(self):
        pass


class Organism:

    def __init__(self, dna, mutate_probability):
        self.dna = dna
        self.mutate_probability = mutate_probability

    def mutate(self):


my_chromosome = Chromosome()
organism = DNA()
print(organism.dna)





# class DNA():
#
#     def __init__(self):
#         self.dna = []
#         index = 0
#         while (index < 10):
#             chromosome = Chromosome()
#             chromosome = chromosome.define_chromosome()
#             self.dna.append(chromosome)
#             index += 1
#
#
# class Chromosome():
#
#     def __init__(self):
#         self.chromosome = []
#
#     def define_chromosome(self):
#         index = 0         #is this acceptable to do in python, or is is there a pythonic way to do it?
#         while (index < 10):
#             self.chromosome.append(random.randint(0,1))
#             index += 1
#         return self.chromosome
#
#
#
# class organisme():
#
#     def __init__(self, dna, organism_type, environment):      #where environment is the % change of a gene changing
#         self.dna = dna
#         self.environment = environment
#         self.organism_type = organism_type
#
#     def mutate(self):
#         index = 0
#         while (index < self.environment):
#             chromosome_index = random.randint(0,9)               # pick random chromosome
#             random_chromosome = self.dna[chromosome_index]
#             gene_index = random.randint(0,9)                     # pick random gene
#             if random_chromosome[gene_index] == 0:
#                 random_chromosome[gene_index] = 1
#             # else:                                              # if mutation truly random and genes can switch in both
#             #     random_chromosome[gene_index] = 0              # directions than it almost always takes over a million generations
#             random_chromosome = self.dna[chromosome_index]
#             index += 1
#         return self.dna
#
#     def check_dna(self):
#         for chromosome in self.dna:
#             if 0 in chromosome:
#                 return False
#         return True
#
#
#     def evolve(self):
#         generation = 0
#         while generation < 500:
#             if self.check_dna() == False:
#                 self.mutate()
#                 generation += 1
#             else:
#                 print(f' {self.organism_type} evolved to have a genome of all ones in {generation} generations')
#                 return generation
#         print(f'{self.organism_type} took over a million generations to get a sequence of all ones')
#         print(f'{self.organism_type} took over a million generations to get a sequence of all ones')
#
#
#
#
# def main():
#     organism1 = DNA()                 # TODO find a cleaner, less repetitive way to do this
#     organism2 = DNA()
#     organism3 = DNA()
#     organism1 = organisme(organism1.dna, "neanderthal", 4)
#     organism2 = organisme(organism2.dna, "ape", 2)
#     organism3 = organisme(organism3.dna, "homosapien", 10)
#
#     organism1.evolve()
#     organism2.evolve()
#     organism3.evolve()
#
