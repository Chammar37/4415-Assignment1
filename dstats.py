import csv
import sys

def numOfBus (data_file, city): 
    # number of business
    with open(data_file, encoding='utf8', mode='r') as business:#open file to read
        yelp_data = csv.reader(business, delimiter=",") #read file through yelp_data variable
        # number of businesses
        counter = 0

        for row in yelp_data:
            if row[4] == city:
                counter += 1
    
    return counter


def avgStars(data_file, city):
    with open(data_file, encoding='utf8', mode='r') as business:#open file to read
        yelp_data = csv.reader(business, delimiter=",") #read file through yelp_data variable
        
        counter = 0
        starsCount = 0.0

        for row in yelp_data:
            if row[4] == city:
                starsCount += float(row[9])
                counter += 1

    return starsCount / counter


def numOfRestaurants(data_file, city):
    with open(data_file, encoding='utf8', mode='r') as business:#open file to read
        yelp_data = csv.reader(business, delimiter=",") #read file through yelp_data variable
        
        restCount = 0
        
        for row in yelp_data:
            if row[4] == city and "Restaurant" in row[12]:
                restCount += 1
        

    return restCount


def avgStarsRestaurants(data_file, city):
    with open(data_file, encoding='utf8', mode='r') as business:#open file to read
        yelp_data = csv.reader(business, delimiter=",") #read file through yelp_data variable
 
        counter = 0 
        resStarsCount = 0.0

        for row in yelp_data:
            if row[4] == city and "Restaurant" in row[12]:
                resStarsCount += float(row[9])
                counter += 1

    return resStarsCount / counter

def avgNumOfReviews(data_file, city):
    # Review Counters
    review_counter = 0
    total_bus = 0
    avg_res_review = 0

    with open(data_file, 'r', encoding='utf8') as business:#open file to read
        yelp_data = csv.reader(business, delimiter=",") #read file through yelp_data variable

        for row in yelp_data:
            if row[4] == city:
                review_counter += int(row[10])
                total_bus += 1
    
    if (review_counter != 0 and total_bus != 0):
        avg_res_review = review_counter / total_bus

    return avg_res_review

def avgNumOfReviewsBus(data_file, city):
    # Review Counters
    review_counter = 0
    res_counter = 0
    avg_res_review = 0

    with open(data_file, 'r', encoding='utf8') as business:#open file to read
        yelp_data = csv.reader(business, delimiter=",")

        for row in yelp_data:
            if row[4] == city and 'Restaurants' in row[12]:
                review_counter += int(row[10])
                res_counter += 1
    
    if (review_counter != 0 and res_counter != 0):
        avg_res_review = review_counter / res_counter

    return avg_res_review

def main():
    # Arugment Validations
    if (len(sys.argv) == 0):
        print("Error: There are not arugments!")
    elif (len(sys.argv) == 1):
         print("Error: No Data file was choosen!")#"yelp-data/yelp-data/yelp_business.csv"
    elif (len(sys.argv) == 2):
         print("Error: No City file was choosen!")
    else:
        # Running the data found
        data_file = sys.argv[1]
        city = sys.argv[2]
        
        # numOfBus
        print("The number of business in " + city + " are " + str(numOfBus(data_file, city)) + "\n")
        # avgStars
        print(str(avgStars(data_file, city)))
        # Num of Restaurants
        print("\nThe average number of reviews for restaurants in " + city + str(numOfRestaurants(data_file, city)))
        #avg Stars Restaurants
        print("\nThe average number of stars for all the Restaurants in " + city + str(avgStarsRestaurants(data_file, city)) )
        #Avg Number of Reviews
        print("\nThe average number of reviews for all business in "+ city + str(avgNumOfReviews(data_file, city)))
        #Average Number of Reviews for Restaurants
        print("\nThe average number of reviews for all restaurants in "+ city + str(avgNumOfReviewsBus(data_file, city))) 

if __name__ == "__main__":
    main()

