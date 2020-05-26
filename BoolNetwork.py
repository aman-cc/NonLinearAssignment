N = 4   # Number of nodes
K = 1   # Number of inputs per node

P = [ [2], [0], [3], [0]]  # Contains parents of ith node; each P[i] needs to be of size K

# F contains update function[i] for node[i]; each F[i] needs to be of size 2^K
F = [ [1, 0],
      [1, 0],
      [0, 1],
      [0, 1] ]

"""
N = 5   # Number of nodes
K = 3   # Number of inputs per node

P = [ [2,3,4], [0,2,4], [1,2,3], [0,2,3], [1,2,4] ]  # Contains parents of ith node; each P[i] needs to be of size K

F = [ [1,0,1,1,0,1,0,1],
      [0,1,0,0,1,0,1,0],
      [0,1,0,1,1,1,0,1],
      [1,1,0,0,0,1,0,0],
      [0,1,0,1,1,1,0,0], ]
"""

def evolution(node):
    states = []
    states.append( node )
    while 1:
        nextnode = []
        for i in range(N):
            # Generate decimal of parent
            temp = []
            for j in range(len(P[i])):
                temp.append( node[P[i][j]] )
            p_value = bin2dec(temp)
            nextnode.append( F[i][ p_value ] )
        node = nextnode
        if node in states:
            states.append(node)
            break
        states.append(node)
    return states

def decimalToBinary(n):  
    return bin(n).replace("0b", "")

def dec2bin(num, l):
    s1 = decimalToBinary(num)
    s2 = ""
    for i in range(l - len(s1)):
        s2 += "0"
    s1 = s2 + s1
    arr  = []
    for i in range(len(s1)):
        arr.append(int(s1[i]))
    return arr

def bin2dec(arr):
    l = len(arr)
    out = 0
    for i in range(l):
        out += arr[i] * ( 2 ** (l-i-1) )
    return out

l = len( decimalToBinary(2**N - 1))
total_states = []
for i in range(2**N):
    total_states.append(dec2bin(i , l))

evol = []
for i in range(len(total_states)):
    evol.append(evolution(total_states[i]))
evol2 = []
for i in range(len(evol)):
    temp2 = []
    for j in range(len(evol[i])):
        temp2.append( bin2dec(evol[i][j]))
    evol2.append(temp2)

attractor= []
for x in evol2:
    if x[0] == x[-1]:
        attractor.append(x)
attractor_list = []

for x in attractor:
    for y in x:
        if y not in attractor_list:
            attractor_list.append(y)
            non_goe_states = []
for x in evol2:
    for y in x[1:-1]:
        if y not in non_goe_states:
            non_goe_states.append(y)
print(evol2)

states = []
goe_states = []
for i in range(2**N):
    states.append(i)
for x in states:
    if x not in non_goe_states:
        goe_states.append(x)

if attractor_list != []:
    print(len(attractor_list),"attractors found are", attractor_list)
else:
    print("No attractor found")

if goe_states != []:
    print(len(goe_states),"Garden of Eden states found are", goe_states)
else:
    print("No Garden of Eden states found")

