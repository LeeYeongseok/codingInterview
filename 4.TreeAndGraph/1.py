import sys

class graph:
    def __init__(self):
        self.vertex = []
        
    def addVertex(self, line):
        self.vertex.append(line)
        
    def printVertex(self):
        print(self.vertex)
    
    
    def dfs(self, start, end):
        self.visted.add(start)
        for l in self.vertex:
            if l[0] == start:
                if l[1] == end:
                    return True
                else:
                    if l[1] not in self.visted and self.dfs(l[1],end):
                        return True
        return False
                
    
    def checkVertex(self, start, end):
        self.visted = set()
        return self.dfs(start, end)
        
        
test = graph()

test.addVertex([1,2])
test.addVertex([1,3])
test.addVertex([1,4])
test.addVertex([4,3])
test.addVertex([4,5])
test.addVertex([4,6])
test.addVertex([5,8])
test.addVertex([7,8])
test.addVertex([7,9])
test.addVertex([9,1])

test.printVertex()
print(test.checkVertex(9,2))
