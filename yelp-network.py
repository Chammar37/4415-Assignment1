import csv
import sys

def drawEdges(data_file):
    with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")
    
        for row in yelp_data:
            
            if row[4] != 'None':
                # Split the friends 
                spliting_friends = row[4].split(",")

                social_network = open('yelp-network.txt', 'a')

                # print(spliting_friends)

                for friend in spliting_friends:
                    # print(row[0] + ' ' + str(friend) + "\n")
                    # print("\n")
                    social_network.write(row[0] + ' ' + str(friend) + "\n") 

                social_network.close()

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

        drawEdges(data_file)

if __name__ == "__main__":
    main()