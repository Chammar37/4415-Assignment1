import csv
import sys

def numOfBus (data_file, city): 
    # number of business
    with open(data_file, encoding='utf8', mode='r') as business:#Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(business, delimiter=",") #Read file through yelp_data variable and set delimeter to ,
        # number of businesses
        counter = 0 #initialize counter to 0

        for row in yelp_data: #Looping through each row of the data
            if row[4] == city: #Access column 4, which the cities are labelled, and check if it is equal to the paramter sent 'city'
                counter += 1 #if so, increase counter by 1
    
    return counter #return the occurences of city


def avgStars(data_file, city):
    with open(data_file, encoding='utf8', mode='r') as business:#Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(business, delimiter=",") #Read file through yelp_data variable and set delimeter to ,
        
        counter = 0 #Initialize counter to 0
        starsCount = 0.0 #Initalize float 

        for row in yelp_data: #Looping through each row of the data
            if row[4] == city: #Access column 4, which the cities are labelled, and check if it is equal to the paramter sent 'city'  
                starsCount += float(row[9]) #Increase stars count by the value in column 9
                counter += 1 #If so, increase counter by 1

    return "{:.2f}".format(starsCount / counter) #Remove all excess and round to 2decimals spots, return value


def numOfRestaurants(data_file, city):
    with open(data_file, encoding='utf8', mode='r') as business: #Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(business, delimiter=",") #Read file through yelp_data variable and set delimeter to ,
        
        restCount = 0 #Initialize restaurant counter to 0 
        
        for row in yelp_data: #Looping through each row of the data
            if row[4] == city and "Restaurant" in row[12]: #Check if city we are currently looking at is equivalent to the sent parameter and if the business is a restaurant
                restCount += 1 #If so, increase the counter by 1 
        

    return restCount #Return restaurant count 


def avgStarsRestaurants(data_file, city):
    with open(data_file, encoding='utf8', mode='r') as business: #Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(business, delimiter=",") #Read file through yelp_data variable and set delimeter to ,
 
        counter = 0 #Initialize restaurant counter to 0
        resStarsCount = 0.0 #Initialize restaurant stars float counter to 0

        for row in yelp_data: #Looping through each row of the data
            if row[4] == city and "Restaurant" in row[12]: #Check if city we are currently looking at is equivalent to the sent parameter and if the business is a restaurant
                resStarsCount += float(row[9]) #Increase stars count by the value in column 9
                counter += 1 #If so, increase counter by 1

    return "{:.2f}".format(resStarsCount / counter) #Remove all excess and round to 2decimals spots, return value

def avgNumOfReviews(data_file, city): 
    # Review Counters
    review_counter = 0 #Initialize number of review counters
    total_bus = 0 #Initialize counter for all businesses
    avg_res_review = 0 #Initialize average restaurant review stars

    with open(data_file, 'r', encoding='utf8') as business: #Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(business, delimiter=",") #Read file through yelp_data variable and set delimeter to ,

        for row in yelp_data: #Looping through each row of the data
            if row[4] == city: #Access column 4, which the cities are labelled, and check if it is equal to the paramter sent 'city'  
                review_counter += int(row[10]) #Increase counter of reviews by the review value seen in the csv
                total_bus += 1 #Add another business being analyzed to the total business counter 
    
    if (review_counter != 0 and total_bus != 0): #As long reviews counted and total business isn't 0, computer the average
        avg_res_review = review_counter / total_bus #Formula to computer average

    return "{:.2f}".format(avg_res_review) #Remove all excess and round to 2decimals spots, return value

def avgNumOfReviewsBus(data_file, city):
    # Review Counters
    review_counter = 0 #Initialize number of review counters
    res_counter = 0 #Initialize restaurant counter 
    avg_res_review = 0 #Initialize average restaurant review

    with open(data_file, 'r', encoding='utf8') as business: #Open the file in read mode (sent by command line paramter)
        yelp_data = csv.reader(business, delimiter=",") #Read file through yelp_data variable and set delimeter to ,

        for row in yelp_data: #Looping through each row of the data
            if row[4] == city and 'Restaurants' in row[12]: #Check if city we are currently looking at is equivalent to the sent parameter and if the business is a restaurant
                review_counter += int(row[10]) #Increase counter of reviews by the review value seen in the csv
                res_counter += 1 #Restaurant counter 
    
    if (review_counter != 0 and res_counter != 0): #As long reviews counted and restaurant business isn't 0, computer the average
        avg_res_review = review_counter / res_counter #Formula to computer average

    return "{:.2f}".format(avg_res_review) #Remove all excess and round to 2decimals spots, return value

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
        
        # numOfBus
        print("The number of business in " + city + " is " + str(numOfBus(data_file, city)) + "\n")
        # avgStars
        print("The average number of stars of a business in " + city +" are " + str(avgStars(data_file, city)))
        # Num of Restaurants
        print("\nThe average number of reviews for restaurants in " + city + " is " + str(numOfRestaurants(data_file, city)))
        #avg Stars Restaurants
        print("\nThe average number of stars for all the Restaurants in " + city + " is " + str(avgStarsRestaurants(data_file, city)) )
        #Avg Number of Reviews
        print("\nThe average number of reviews for all business in "+ city + " is " + str(avgNumOfReviews(data_file, city)))
        #Average Number of Reviews for Restaurants
        print("\nThe average number of reviews for all restaurants in "+ city + " is " +str(avgNumOfReviewsBus(data_file, city))) 

#Establish the main method
if __name__ == "__main__":
    main()

