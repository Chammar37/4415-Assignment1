import csv
import sys
import matplotlib.pyplot as plt

def restaurantCategoryDist (data_file, city):

    with open(data_file, 'r', encoding='utf8') as business: #Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(business, delimiter=",") #set delimeter to ,

        # Dict & Row
        restaurant_dict = {} #Initialize the restaurant hash-table/dictionary
        spliting_row = "" #Initialize the string variable which holds all split rows

        for row in yelp_data: #Looping through each row of the data
            if row[4] == city and 'Restaurants' in row[12]: #Check if city we are currently looking at is equivalent to the sent parameter and if the business is a restaurant
                # Splitting Row into pieaces 
                spliting_row = row[12].split(";") #Split the list based on when we see a ';'
                # Adding the pieces into Dict
                for key in spliting_row: #Iterate through the split values
                    if (key == "Restaurants"): #Check if value being analyzed is equal to string 'Restaurants'
                        continue
                    elif (key in restaurant_dict.keys()): #If the key already exists in keys list
                        restaurant_dict[key] += 1 #Increment counter by 1 at the specific hash
                    else:
                        restaurant_dict[key] = 1 #If it doesn't exist establish it to 1

    return dict(sorted(restaurant_dict.items(), key=lambda item: item[1], reverse=True)) #Return sorted dictionary

def restaurantReviewDist (data_file, city):
    with open(data_file, 'r', encoding='utf8') as business: #Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(business, delimiter=",") #set delimeter to ,

        # Dict & Row
        restaurant_dict = {} #Initialize dictionary for all restaurants
        spliting_row = ""  #Initialize the string variable which holds all split rows

        for row in yelp_data: #Looping through each row of the data
            if row[4] == city and 'Restaurants' in row[12]: #Check if city we are currently looking at is equivalent to the sent parameter and if the business is a restaurant
                # Splitting Row into pieaces 
                spliting_row = row[12].split(";") #Split the list based on when we see a ';'
                # Adding the pieces into Dict
                for key in spliting_row: #Iterate through the split values
                    if (key == "Restaurants"): #Check if value being analyzed is equal to string 'Restaurants'
                        continue
                    elif (key in restaurant_dict.keys()): #If the key already exists in keys list
                        restaurant_dict[key][0] += int(row[10]) #Increment value at hash key seen at column 10
                        restaurant_dict[key][1] += float(row[9]) #Increment value at hash key seen at column 9

                    else:
                        restaurant_dict[key] = [int(row[10]), float(row[9])] #If it doesn't already exist in the list, add at [key]

        # Finding Average of the stars
        star_counter_list = restaurantCategoryDist(data_file, city) #Call method to identify restaurant category
        for key in restaurant_dict.keys(): #loop throw keys in dictionary
            restaurant_dict[key][1] = restaurant_dict[key][1] / star_counter_list[key] #Assign value at the hash value

    return dict(sorted(restaurant_dict.items(), key=lambda item: item[1], reverse=True)) #Return sorted dictionary


def main(): #Main method to manage command line arguments, files being sent and calling methods. 
    # Arugment Validations
    if (len(sys.argv) == 0): #If no arguments are sent, print this comment to the user
        print("Error: There are not arugments!") #User must add at least 3 arguments!
    elif (len(sys.argv) == 1): #If only 1 argument is sent, print this comment to the user
         print("Error: No Data file was choosen!") #User must add at least 3 arguments!
    elif (len(sys.argv) == 2): #If only 2 argument is sent, print this comment to the user
         print("Error: No City file was choosen!") #User must add at least 3 arguments!
    else:
        # Running the data found
        data_file = sys.argv[1] #The data being analyzed will be grabbed from the users input and saved for later use
        city = sys.argv[2] #The city being analyzed will be grabbed from the users input and saved for later use

        # print category
        print("\ncategory:#restaurants")

        category_dict = list(restaurantCategoryDist(data_file, city).items())[:10] #Get top 10 of restaurant category
        category = [] #Initialize array for categories
        category_counter = [] #Initialize array for categories in counter

        for key in category_dict: #Loop through category dictionary
            category.append(key[0]) #Append all keys at first index to list
            category_counter.append(key[1]) #Append all keys at second index to list
            print(key[0] + ":" + str(key[1])) #Print result

        #Print review
        print("\ncategory:#reviews:avg_stars") #Print title and format
        review_dict = list(restaurantReviewDist(data_file,city).items())[:10] #Get top 10 of restaurant review 
        
        for key in review_dict: #loop through review dictionary 
            print(key[0] + ":" + str(key[1][0]) + ":"+ str("{:.1f}".format(key[1][1]))) #Print out result and round to nearest decimal for review 

         # Draw the Bar Graph
        plt.figure(figsize=(16, 5))
        plt.bar(category,category_counter)
        plt.title("Restaurant Category Distribution")
        plt.xlabel("Categories")
        plt.ylabel("Number of Restaurant")
        plt.show()
        
#Establish the main method
if __name__ == "__main__":
    main()