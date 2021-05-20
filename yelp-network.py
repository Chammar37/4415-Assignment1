import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt

def drawEdges(data_file):
    # Graph
    G = nx.Graph()

    with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")
    
        for row in yelp_data:
            
            if row[4] != 'None':
                # Split the friends     
                # spliting_friends = row[4].split(",")
                splitting_dict = {}
                # row[4].split(",")

                # To add the data in TXT file
                # social_network = open('yelp-network.txt', 'a')
                # social_network.close()

                # print(spliting_friends)
                # print(row[4].split(","))
                # Add user
                if not row[0] in splitting_dict.keys():
                    friends = row[4].split(",")
                    for friend in friends:
                        splitting_dict[row[0]] = friend
                        
                # for friend in spliting_friends:
                #      # Add User frined
                #     if friend not in G.nodes():
                #         G.add_node(friend)
                    
                #     G.add_edge(row[0], friend)


                    # social_network.write(row[0] + ' ' + str(friend) + "\n") 
        

        print(splitting_dict)

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