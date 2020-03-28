from Chromosome import Chromosome
from Fitness import fitnessFc
from RW import RW
from GA import GA
from Solver import solveTSP
from matplotlib import pyplot as plt
from random import shuffle

def main():
    reader=RW("testData/berlin.txt")
    graph= reader.readFile()
    ga = GA(80, graph)
    solution=solveTSP(ga,2000)
    solution[0].renumber()
    reader.writeToFile(solution[0])
    plt.plot(solution[1])
    plt.show()
main()