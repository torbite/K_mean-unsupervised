import matplotlib.pyplot as plt
import math
def dst(p1, p2):
    dimns = []
    if len(p1) != len(p2):
        print(p1, p2)
        raise ValueError("Points must have the same number of dimensions")
    for x1, x2 in zip(p1, p2):
        
        dimns.append((x1 - x2)**2)
    
    a= sum(dimns)
    result = math.sqrt(a)
    return result
 

def sumPts(p1, p2):
    i = 0
    soma = [0] * len(p1)
    for a, b in zip(p1,p2):
        soma[i] = a + b
        i += 1
    return soma


def avgPoints(points):
    
    a = points[0]
    
    for i in range(len(points)):
        if i == 0:
            
            a = points[0]
            
        else:
            
            a = sumPts(a, points[i])
            if a == []:
                print("ad", a)
    
    
    for i in range(len(a)):
        a[i] = a[i] / len(points)
    return a


