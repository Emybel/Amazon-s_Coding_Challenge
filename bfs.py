import queue
import numpy as np

#Global variables
# R = Number of rows / C = Number of columns

R = 10 
C = 10 

# (10*10) grid
mgrid=np.zeros((R,C))
mgrid[7,9] = 1
mgrid[7,8] = 1
mgrid[7,7] = 1
mgrid[8,7] = 1
mgrid[0,0] = 0
mgrid[9,9] = "DP"

sr = mgrid(0)
sc = mgrid([0])


#Variables used to truck the numbers of steps taken
move_vount = 0
nodes_left_in_layer = 1 # Trcks how many nodes we need to dequeue before taking a step
nodes_in_next_layer = 0 # Tracks how many nodes we added in BFS expension so that we could update nodes left il layer accordingly in the next iteration

# Direction vectors 
dr = np.array([1,1,1,0,-1,-1,-1,0])
dc = np.array([1,0,-1,-1,-1,0,1,1])

#reconstruct path going backwards from delivery point 

#Exploring neighbours 

#def explor_neighbour(rr,cc) :
#h = 0 
#for h in range(8) :


# Queues for rows and columns
rq = queue()
cq = queue()
reached_end = False # Variable track wether the delivery point is reached or not during the BFS

# Visited grid of false values used to track wether the node at position (i,j) has been visited
visited = np.zeros([R*C], dtype=bool)

# Grid to save path
pnode = np.zeros(R*C)
rq.put(sr)
cq.put(sc)
visited [sr,sc] = True
while rq.size() > 0 and cq.size() >0 : # While the queues are not empty we keep poping from the queue to explore noeds
    r = rq.pop()
    c = cq.pop()
    if mgrid[r,c] == "DP" :
        reached_end = True
    break
pnode = mgrid[r,c]

def eplore_neighbour(,)



    
    



