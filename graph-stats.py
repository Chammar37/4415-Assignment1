import csv
import sys
import networkx as nx

def graph_stats (data_file):
    # Nodes and Edges Dict
    network_graph = {}

    with open(data_file, 'r', encoding='utf8') as friends:
        yelp_data  = csv.reader(friends, delimiter=",")

        for col in yelp_data:
            if (col[0] != 'user_id friends'):
                # Split frineds 
                spliting_nodes = col[0].split(' ')

                if spliting_nodes[0] not in network_graph.keys():
                    network_graph[spliting_nodes[0]] = 1
                else:
                    network_graph[spliting_nodes[0]] += 1
                if spliting_nodes[1] not in network_graph.keys():
                    network_graph[spliting_nodes[1]] = 1
                else:
                    network_graph[spliting_nodes[1]] += 1

    number_of_nodes = len(network_graph.keys())
    number_of_edges = 0
    print("Number of nodes: " + str(number_of_nodes))
    
    for node in network_graph.keys():
        number_of_edges += network_graph[node]
    number_of_edges = int(number_of_edges / 2)
    print("Number of edges: " + str(number_of_edges))
    
    # nodeDegree(network_graph)
    print(avgNodeDegree(number_of_nodes, number_of_edges))

def nodeDegree(network_graph):
    for key, value in sorted(network_graph.items(), key=lambda item: item[1], reverse=True):
        print(key + ": " + str(value))

def avgNodeDegree(number_of_node, number_of_edge):
    avgNodeDegree = (number_of_edge * 2) / number_of_node
    return "avgNodeDegree:" + str(avgNodeDegree)

def main():
    # Arugment Validations
    if (len(sys.argv) == 0):
        print("Error: There are not arugments!")
    elif (len(sys.argv) == 1):
         print("Error: No Data file was choosen!")
    else:
        # Increase Field Size so there is no out of limit error
        csv.field_size_limit(sys.maxsize)

        # Running the data found
        data_file = sys.argv[1]

        graph_stats(data_file)

if __name__ == "__main__": 
    main()