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


    def __str__(self):
        return f"{self.chromosome}"

    def __repr__(self):
        return f'{self.chromosome}'

    def chose_gene_to_mutate(self):
        gene = self.chromosome[random.randint(0, 9)]
        gene.mutate()


class DNA:

    def __init__(self):
        self.dna = [Chromosome() for i in range(10)]

    def choose_chromosome_to_mutate(self):
        chromosome = self.dna[random.randint(0, 9)]
        chromosome.chose_gene_to_mutate()


class Organism:

    def __init__(self, dna, mutate_probability):
        self.dna = dna
        self.mutate_probability = mutate_probability

    def __str__(self):
        return f"{self.dna}"

    def __repr__(self):
        return f'{self.dna}'

    def mutate_dna(self):
        for gene in range(self.mutate_probability):
            dna.choose_chromosome_to_mutate()

    def check_if_mutated(self):
        generations = 0
        if generations < 1000000:
            for chromosome in self.dna.dna:
                print(chromosome.chromosome)
                for gene in chromosome.chromosome:
                    print(gene)
                    if gene == 0:
                        self.mutate_dna()
                        generations += 1
                    else:
                        print("evolution successful")
                        return generations
        print('Took over a million generations to mutate')


# def establish_dna_object():   todo - find way to encorportate this
#     dna_list = []                    logic for declaring both DNA objects
#                                      and organisms
#     for dna in range(3):
#         dna = DNA()
#         dna_list.append(dna)
#     return dna_list

dna1 = DNA()
dna2 = DNA()
dna3 = DNA()
organism1 = Organism(dna1, 5)
organism2 = Organism(dna2, 10)
organism3 = Organism(dna3, 20)

organisms = [organism1, organism2, organism3]

for organism in organisms:
    print(organism.check_if_mutated())


