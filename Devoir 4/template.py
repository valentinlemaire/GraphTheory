"""
    Solution for the fourth homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math


# ------------------------------
# Tests (should be correct)
# ------------------------------
# is_reachable = [[0,0,1,0,0,1], [0,0,1,0,1,0], [1,1,0,0,0,0], [0,0,0,0,0,0], [0,1,0,0,0,0], [1,0,0,0,0,0]]   ;   solution = 2
# is_reachable = [[0,0,1,0,0,0], [0,0,1,0,0,0], [1,1,0,1,1,1], [0,0,1,0,0,0], [0,0,1,0,0,0], [0,0,1,0,0,0]]   ;   solution = 1
# is_reachable = [[0,0,1,0,0,1], [0,0,0,0,0,0], [1,0,0,0,1,0], [0,0,0,0,0,0], [0,0,1,0,0,0], [1,0,0,0,0,0]]   ;   solution = 2
# is_reachable = [[0,0,1,0,0,1], [0,0,0,0,1,0], [1,0,0,0,1,0], [0,0,0,0,0,0], [0,1,1,0,0,0], [1,0,0,0,0,0]]   ;   solution = 2
# is_reachable = [[0,0,1,0,0,1], [0,0,0,1,1,0], [1,0,0,0,1,0], [0,1,0,0,0,0], [0,1,1,0,0,0], [1,0,0,0,0,0]]   ;   solution = 3

    
def matching(T, friends, hiding_places):
    """ 
    INPUT : 
        - T, the number of seconds
        - friends, a list of tuples (x, y, v) describing the position (x, y) and velocity v
          of each friend
        - hiding_places, a list of tuple (x, y) giving the position (x, y) of each hiding place
    OUTPUT :
        - return the maximal number of friends that can hide from the game master
        
        See homework statement for more details
    """
    reachable = lambda T, friend, hiding_place : (friend[0]-hiding_place[0])**2 + (friend[1]-hiding_place[1])**2 <= (T*friend[2])**2 

    is_reachable = [[reachable(T, f, h) for h in hiding_places] for f in friends]
    edge_in_coupling = [[False for _ in hiding_places] for _ in friends]

    friends_coupled = [False] * len(friends)
    places_coupled = [False] * len(hiding_places)

    couple = [-1] * len(friends)

    N = 0
    done = False

    for i in range(len(friends)):
        for j in range(len(hiding_places)):
            if (is_reachable[i][j]) and (not friends_coupled[i]) and (not places_coupled[j]):
                couple[i] = j
                friends_coupled[i], places_coupled[j] = True, True
                N += 1
                break

    while not done:
        c = [-1]
        first_ensemble = -1 
        for i in range(len(friends)):
            if not friends_coupled[i]:
                c[0] = i
                first_ensemble = 0
        if c[0] == -1:
            for j in range(len(hiding_places)):
                if not hiding_places[j]:
                    c[0] = j
                    first_ensemble = 1
        finished = False
        while not finished:
            if first_ensemble == 0:
                for i in range(len(friends)):
                    pass
    return N

    
if __name__ == "__main__":

    # Read Input
    
    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m, T = int(l[0]), int(l[1]), int(l[2])
        
        friends = []
        for friend in range(n):
            l = fd.readline().rstrip().split()
            friends.append(tuple([float(x) for x in l]))
       
        hiding_places = []
        for hiding_place in range(m):
            l = fd.readline().rstrip().split()
            hiding_places.append(tuple([float(x) for x in l]))

    # Compute answer 
     
    ans = matching(T, friends, hiding_places)
     
    # Check results 

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans:
            print("Test sample : Correct")
        else:
            print("Test sample : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output)) 
        
