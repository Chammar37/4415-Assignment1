import csv
import sys
import networkx as nx

def graph_stats (data_file):
    #Initialize the network dictionary 
    network_graph = {}

    with open(data_file, 'r', encoding='utf8') as friends: #Open the file in read mode (sent by command line paramter)
        yelp_data  = csv.reader(friends, delimiter=",") #set delimeter to ,

        for col in yelp_data: #Looping through data saved in csv data file. Contain each column as an index
            if (col[0] != 'user_id friends'): #Ignore the first row in the .txt file, jump to the first and friend
                # Split frineds 
                spliting_nodes = col[0].split(' ') #Split friends by space. It will now contain each user/friend pair

                if spliting_nodes[0] not in network_graph.keys(): #If first user is not in the keys list, establish the key and set the count for that specific key to 1
                    network_graph[spliting_nodes[0]] = 1 #Setting the the value to 1 for that new key
                else:
                    network_graph[spliting_nodes[0]] += 1 #If the user is already in the list, increase the counter for that specific key 
                if spliting_nodes[1] not in network_graph.keys(): #If second user is not in the keys list, establish the key and set the count for that specific key to 1
                    network_graph[spliting_nodes[1]] = 1 #Setting the the value to 1 for that new key
                else:
                    network_graph[spliting_nodes[1]] += 1 #If the user is already in the list, increase the counter for that specific key 

    number_of_nodes = len(network_graph.keys()) #Retrieve the number of nodes for the Graph 
    number_of_edges = 0 #Set the number of edges 
    print("Number of nodes: " + str(number_of_nodes)) #Print out the number of nodes
    
    for node in network_graph.keys(): #Loop through keys in the established network graph
        number_of_edges += network_graph[node] #Accumulate the numner of edges of the established network graph
    number_of_edges = int(number_of_edges / 2) #Concatenate to a int after dividing by 2. This is due to our algorithm and the Edge formula when calculated all edges every 2 nodes.
    print("Number of edges: " + str(number_of_edges)) #Print out the number of edges
    
    # nodeDegree(network_graph)
    print(avgNodeDegree(number_of_nodes, number_of_edges)) #Call function to calculate average node degree.

def nodeDegree(network_graph): #Retrieve graph
    for key, value in sorted(network_graph.items(), key=lambda item: item[1], reverse=True): #Loop through established network and sort print layout based on a decreasing characeristic. Starting with the node with the highest degree.
        print(key + ": " + str(value)) #Print key value, aka "User" : "Node Degree"

def avgNodeDegree(number_of_node, number_of_edge): #Retrieve node and edge amount
    avgNodeDegree = (number_of_edge * 2) / number_of_node #Calculate average node degree of whole graph
    return "avgNodeDegree:" + str(avgNodeDegree) #Return print statement of average node degree of whole graph

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

        graph_stats(data_file) #Call method to draw the graph and send the file to analyze. 

#Establish the main method.
if __name__ == "__main__": 
    main()