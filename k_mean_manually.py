import matplotlib.pyplot as plt
import matplotlib.colors as matcol
import random
import cartesianCalc as cart
import copy

class Point():
    def __init__(self, position = [0,0], color = "black", myK = None):
        self.position = position
        self.color = color
        self.k = myK
    
    def setRandomPosition(self):
        
        
        self.position = [random.randint(0,1500),random.randint(0,1500)]
    
    def getClosestK(self, ks):
        dists = {}
        
        for k in ks:
            try:
                
                dists[k] = cart.dst(self.position, copy.deepcopy(k.position))
            except Exception as ex:
                print(k.position)
                raise ex
        closest = min(dists, key=dists.get)
        self.color = closest.color
        self.k = closest
        


class K():
    def __init__(self, position = [0,0], color = "blue"):
        self.position = position
        self.color = color
    
    def setRandomPosition(self):
        self.position = [random.randint(0,30), random.randint(0,30)]


def plot_points(points, colr, mk):

    x_coords, y_coords = zip(*points)
    

    plt.scatter(x_coords, y_coords, color=colr, marker=mk)
    

    plt.xlabel('X2')
    plt.ylabel('X1')
    plt.title('Points on a Graph')
    plt.grid(True)
color_names =  ["red","blue","green","orange","purple","pink","brown","black","gray","cyan","magenta","lime","indigo","violet","gold","silver","maroon","navy"]

points = []
for i in range(1000):
    points.append(Point())
for i in points:
    i.setRandomPosition()
print()
amount_of_ks = int(input('How manny clusters do you want to have? (number from 1 to 18) \nR: '))

ks = [K(color=color_names[i],position=[0,0]) for i in range(amount_of_ks)]


for i in ks:
    i.setRandomPosition()


def J(ks, nbrs):
    
    n = len(ks)
    ka = 0
    m =0
    for i in range(n):
        m += len(nbrs[i])
        
        for pt in nbrs[i]:
            ka += cart.dst(copy.deepcopy(ks[i].position), pt)**2
    err = ka/m
    return err

error = 0
oldError = 0
for z in range(100):
    for i in points:
        i.getClosestK(ks)
    
    
    k_pts_list = {}
    for k in ks:
        k_pts_list[k] = []
    


    for i in points:
        
        if i.k in list(k_pts_list.keys()):
            
            k_pts_list[i.k].append(copy.deepcopy(i.position))
    

    
    for k in ks:
        
        if k_pts_list[k] != []:
            k.position = cart.avgPoints(k_pts_list[k])
    

    nbrs = []
    for i in k_pts_list.keys():
        nbrs.append(k_pts_list[i])
    error = J(ks, nbrs)
    print(f"iteration {z}")
    print("erro: ", error)
    print()
    differr = oldError - error
    
    if differr < 0.25 and differr > -0.25:
        break
    oldError = error
    
print('creating graph...')    

for i in points:
    plot_points([i.position], i.color, 'o')
for i in ks:
    plot_points([i.position], i.color, 'x')

plt.gca().set_facecolor('white')
plt.show()
print('Done')