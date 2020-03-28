import heapq
from random import randint,random, shuffle
from Chromosome import Chromosome
from Fitness import fitnessFc

class GA:
    def __init__(self, popSize=None, problParam=None, eliteSize=30, mutationRate=0.05):
        self.__popSize = popSize
        self.__problParam = problParam
        self.__population=[]
        self.__eliteSize=eliteSize
        self.__mutationRate=mutationRate

    def initialisation(self):
        c = Chromosome(self.__problParam)
        self.__population.append(c)
        for _ in range(0, self.__popSize-1):
            shuffle(c.repres)
            self.__population.append(c)
        heapq.heapify(self.__population)

    def evaluation(self):
        for c in self.__population:
            c.fitness = fitnessFc(c, self.__problParam)


    def bestChromosome(self):
        return self.__population[0]

    def selection(self):
        pos1=randint(0,self.__popSize-1)
        pos2=randint(0,self.__popSize-1)
        if (self.__population[pos1].fitness> self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def tournament(self):
        tournament = []
        for i in range(self.__eliteSize):
            p = randint(0, self.__popSize - 1)
            tournament.append(self.__population[p])
        heapq.heapify(tournament)
        return tournament[0], tournament[1]

    def newPopulation(self):
        newPop = []
        for _ in range(self.__popSize):
            p1,p2=self.tournament()
            off = p1.crossover(p2)
            if random()<=self.__mutationRate:
                off.mutation()
            newPop.append(off)
        heapq.heapify(newPop)
        return newPop


    def oneGeneration(self):
        newGen=self.newPopulation()
        newPop=[]
        i=0
        for i in range(int(self.__popSize/2)+1):
            newPop.append(self.__population[i])
        p=0
        for j in range(i+1,self.__popSize):
            newPop.append(newGen[p])
            p+=1
        self.__population=newPop
        self.evaluation()
        heapq.heapify(self.__population)

