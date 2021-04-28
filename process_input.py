import sys
import numpy as np
from ogb.nodeproppred import NodePropPredDataset

def print_usage():
    print("python process_input.py papers")
    print("python process_input.py products")
    sys.exit()
    
def process(dataset_name):
    if (dataset_name == "papers"):
        dataset = NodePropPredDataset(name = 'ogbn-papers100M', root='parm/')
        outf_name = "papers.graph"
    elif (dataset_name == "products"):
        dataset = NodePropPredDataset(name = 'ogbn-products', root='parm/')
        outf_name = "products.graph"
    else:
        print_usage()
        sys.exit(0)

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

    with open(outf_name, 'w') as fout:
        sys.stdout = fout
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

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print_usage()
        sys.exit(0)
    process(sys.argv[1])

    