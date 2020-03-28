def fitnessFc(c,probParam):
    fit=0
    rep=c.repres
    for i in range(len(rep)-1):
        fit+=probParam['matrix'][rep[i]][rep[i+1]]
    fit+=probParam['matrix'][rep[-1]][rep[0]]
    return fit

