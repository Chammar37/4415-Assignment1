import csv
import sys
import networkx as nx

def graph_stats (data_file):
    # Nodes and Edges
    G = nx.Graph()
    number_of_edges = 0

    with open(data_file, 'r', encoding='utf8') as friends:
        yelp_data  = csv.reader(friends, delimiter=",")

        for col in yelp_data:
            if (col[0] != 'user_id friends'):
                # Split frineds 
                spliting_nodes = col[0].split(' ')
                # Check user and friend node before adding to graph
                if spliting_nodes[0] not in G.nodes():
                    G.add_node(spliting_nodes[0])
                if spliting_nodes[1] not in G.nodes():
                    G.add_node(spliting_nodes[1])

                # G.add_edge(spliting_nodes[0], spliting_nodes[1])
    
    print("Fuck Marc")
    print("Number of nodes: " + len(G.nodes()))
    print("Number of edges: " + len(G.edges()))

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