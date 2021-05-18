import csv
import sys

def restaurantCategoryDist (data_file, city):

    with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")

        # Dict & Row
        restaurant_dict = {}
        spliting_row = ""

        for row in yelp_data:
            if row[4] == city and 'Restaurants' in row[12]:
                # Splitting Row into pieaces 
                spliting_row = row[12].split(";")
                # Adding the pieces into Dict
                for key in spliting_row:
                    if (key == "Restaurants"):
                        continue
                    elif (key in restaurant_dict.keys()):
                        restaurant_dict[key] += 1
                    else:
                        restaurant_dict[key] = 1 

    return sorted(restaurant_dict.items(), key=lambda item: item[1], reverse=True)

def restaurantReviewDist (data_file, city):
     with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")

        # Dict & Row
        restaurant_dict = {}
        spliting_row = ""

        for row in yelp_data:
            if row[4] == city and 'Restaurants' in row[12]:

def main():
    # Arugment Validations
    if (len(sys.argv) == 0):
        print("Error: There are not arugments!")
    elif (len(sys.argv) == 1):
         print("Error: No Data file was choosen!")
    elif (len(sys.argv) == 2):
         print("Error: No City file was choosen!")
    else:
        # Running the data found
        data_file = sys.argv[1]
        city = sys.argv[2]

        # Pretty Printing
        category_List = restaurantCategoryDist(data_file, city)
        prettyPrinting = ""
        
        for item in category_List:
            print(item[0] + ":" + str(item[1]))


if __name__ == "__main__":
    main()