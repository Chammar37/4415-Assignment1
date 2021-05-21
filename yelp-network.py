import csv
import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def drawEdges(data_file):

    G = nx.Graph()  

    # Importing data from Yelp to TXT file
    social_network = open('yelp-networkTest_4.txt', 'w')
    
    with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")
        
        for col in yelp_data:
            if col[4] != 'None':
                # Split friends
                spliting_friends = col[4].split(', ')

                if col[0] not in G.nodes():
                    G.add_node(col[0])

                for friend in spliting_friends:
                    if friend not in G.nodes():
                        social_network.write(col[0] + ' ' + friend + "\n") 
                
    social_network.close()

    print("Fuck Marc")
    

def main():
    # Helper 
    # G = nx.Graph()
    # G.add_node('A')
    # G.add_node('B')
    # G.add_node('C')
    # G.add_edge('A', 'B')
    # G.add_edge('B', 'A')
    # G.add_edge('B', 'C')
    # print(G.nodes())
    # print(G.edges())
    # nx.draw(G)
    # plt.show()

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

        drawEdges(data_file)

if __name__ == "__main__":
    main()