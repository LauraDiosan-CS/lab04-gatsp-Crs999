from EuclidianDistance import euclideanDistance

class RW:
    def __init__(self, filename):
        self.__fileName=filename

    def readFile(self):
        mat = {}
        f = open(self.__fileName, "r")
        if self.__fileName!="testData/berlin.txt":
            n=int(f.readline())
            mat['noNodes']=n
            mat['matrix']=[]
            for i in range(n):
                mat['matrix'].append([])
                elems=f.readline().split(",")
                for e in elems:
                    mat['matrix'][i].append(int(e))
            return mat
        else:
            words=f.readline().split(' ')
            while words[0]!="DIMENSION:":
                words=f.readline().split(' ')
            mat['noNodes']=int(words[1])
            f.readline()
            f.readline()
            lines=[]
            for i in range(0,mat['noNodes']):
                words=f.readline().split(" ")
                lines.append((float(words[1]),float(words[2])))

            mat['matrix']=[[0.0 for i in range(mat['noNodes'])] for j in range(mat['noNodes'])]
            for i in range(0,mat['noNodes']-1):
                for j in range(i+1, mat['noNodes']):
                    mat['matrix'][i][i]=0.0
                    mat['matrix'][j][i]=mat['matrix'][i][j]=euclideanDistance(lines[i],lines[j])
            return mat

    def writeToFile(self, solution):
        f=open("output.txt","w")
        lines=[]
        lines.append(str(len(solution.repres))+"\n")
        rep=str(solution.repres[0])
        for x in solution.repres[1:]:
            rep+=","+str(x)
        lines.append(rep+"\n")
        lines.append(str(solution.fitness))
        f.writelines(lines)


