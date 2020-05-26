Random Boolean Networks
Initialize the first cell of the notebook by giving the following attributes of the network. Sample code for N = 4, K = 1, N = 5, K = 3 is given.

N - Number of nodes <br/>
K - Number of input per node <br/>
P - Array containing parents of each node (needs to be of length N and each P[i] needs to be of length K) <br/>
F - Update functions (needs to be of length N where each F[i] represents update function of i node; F[i] needs to be of length 2^K) <br/>
