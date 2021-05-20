import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt

def drawEdges(data_file):

    with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")
    
        for row in yelp_data:
            
            if row[4] != 'None':
      
                spliting_friends = row[4].split(",")
                # To add the data in TXT file
                social_network = open('yelp-network.txt', 'a')

                for friend in spliting_friends:
                    social_network.write(row[0] + ' ' + friend + "\n")

                social_network.close()

    with open ('yelp-network.txt', 'r', encoding='utf8') as network:
        social_data = csv.reader(network, delimiter=",")
        
        # for row in social_data:
        print(social_data)

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