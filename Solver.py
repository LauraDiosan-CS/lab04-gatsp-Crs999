def solveTSP(ga,noGen):
    ga.initialisation()
    ga.evaluation()
    stop = False
    g = 0
    ga.oneGeneration()
    best = ga.bestChromosome()
    fitnessList=[]
    while (not stop and g < noGen):
        g += 1
        ga.oneGeneration()
        bestChromo = ga.bestChromosome()
        fitnessList.append(bestChromo.fitness)
        print("Generation: "+str(g)+" "+str(bestChromo))
        if best.fitness > bestChromo.fitness:
            best = bestChromo
    return (best, fitnessList)