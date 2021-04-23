import numpy as np
from ogb.nodeproppred import NodePropPredDataset

dataset = NodePropPredDataset(name = 'ogbn-papers100M', root='parm/')
#dataset = NodePropPredDataset(name = 'ogbn-products', root='parm/')
#dataset = NodePropPredDataset(name = 'ogbn-mag', root='parm/')
graph, label = dataset[0]

edge_index = graph['edge_index']

lhs = edge_index[0]
rhs = edge_index[1]

number_nodes = max(max(lhs), max(rhs)) + 1
#print(number_nodes)

matrix = {}
num_edges = 0
for i in range(number_nodes):
    matrix[i] = {i}
    #matrix[i].append(i)
    num_edges = num_edges + 1

for i in range(len(lhs)):
    matrix[lhs[i]].add(rhs[i])

print(number_nodes, num_edges + len(lhs) // 2)

for x in matrix:
    #matrix[x].sort()
    #if matrix[x]==[]:
    #    print(x+1, end=' ')
    for y in matrix[x]:
        if y=='':
            print(y, end=' ')
        else:
            print(int(y)+1, end=' ')
    print()
