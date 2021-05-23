import csv
import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def drawEdges(data_file):
    G = nx.Graph() #Create Graph G using networkx library. For Nodes and Edge management

    # Importing data from Yelp to TXT file
    social_network = open('yelp-network.txt', 'w') #Opening the file in write mode
    
    with open(data_file, 'r', encoding='utf8') as users: #Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(users, delimiter=",") #set delimeter to ,
        
        for col in yelp_data: #Looping through data saved in csv data file. Contain each column as an index
            if col[4] != 'None': #Checking if the current user being analyzed has a list of friends. If so, search through them
                # Split friends
                spliting_friends = col[4].split(', ') #Isoalate each friend seperately 

                if col[0] not in G.nodes(): #If the current user being analyzed is not already in the list of nodes, at it
                    G.add_node(col[0]) #Adding the node to the graph 

                for friend in spliting_friends: #Loop through each friend in the list of friends
                    if friend not in G.nodes(): #If the current friend (of the user) being analyzed is not already in the list of nodes, at it
                                                #This further makes sure that the next time we loop, we are not writing the same edge backwards or twice.
                        social_network.write(col[0] + ' ' + friend + "\n") #Write the user and his friend, if the iteration makes it to this line, the edge has not yet been printed to the file in either 'direction'
                        #This code makes sure the following does not exist in the file 
                        #                   a1 b1
                        #                   b1 a1
                        #Rather, if the edge already exists in the collection of Nodes, it will not be printed again. Both will not exist in the file.
    social_network.close()

def main(): #Main method to manage command line arguments, files being sent and calling methods. 
    # Arugment Validations
    if (len(sys.argv) == 0): #If no arguments are sent, print this comment to the user
        print("Error: There are not arugments!") #User must add at least 2 arguments!
    elif (len(sys.argv) == 1): #If only 1 argument is sent, print this comment to the user
         print("Error: No Data file was choosen!") #User must add at least 2 arguments!
    else:
        # Increase Field Size so there is no out of limit error
        csv.field_size_limit(sys.maxsize)

        # Running the data found
        data_file = sys.argv[1] #The data being analyzed will be grabbed from the users input and saved for later use

        drawEdges(data_file) #Call method to draw the graph and send the file to analyze. 

#Establish the main method.
if __name__ == "__main__":
    main()