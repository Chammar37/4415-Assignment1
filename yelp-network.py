import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt

def drawEdges(data_file):
    # Graph
    G = nx.Graph()

    with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")

        spliting_friends = []

    
        for row in yelp_data:
            
            if row[4] != 'None':
                # Split the friends     
                # spliting_friends = row[4].split(",")
                
                spliting_friends = row[4].split(",")

                for friend in spliting_friends:
                    if ((friend, row[0]) not in spliting_friends):
                        spliting_friends.append((row[0], friend))

                # To add the data in TXT file
                # social_network = open('yelp-network.txt', 'a')
                # social_network.close()

                # print(spliting_friends)

                # Add user
                # for friend in spliting_friends:
                #     #  Add User frined
                #     if friend not in G.nodes():
                #         G.add_node(friend)
                    
                #     G.add_edge(row[0], friend)


                    # social_network.write(row[0] + ' ' + str(friend) + "\n") 
    G = nx.Graph()

    for user in spliting_friends:
        print(user)
        # G.add_node(user[0])
        # G.add_node(user[1])
        # G.add_edge(user[0], user[1])
    
    # social_network = open('yelp-network.txt', 'a')

    # for edge in G.edges():
    # #    social_network.write(edge[0] + ' ' + edge[1] + "\n")
    #     print(edge)


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