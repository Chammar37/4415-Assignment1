import csv
import sys

def restaurantCategoryDist (data_file, city):

    with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")

          # Categories
                #  Chinese,  Japanese,  Korean,  Greek, Persian/Iranian, Indian, Canadian, Mexican, American, Italian, Asian Fusion, French, Other
        category_list = ["Chinese", "Japanese", "Korean", "Greek", "Persian/Iranian", "Indian", "Canadian", "Mexican", "American", "Italian", "Asian Fusion", "French", "Others"]
        restaurant_dict = {
                    "Chinese": 0,
                    "Japanese": 0,
                    "Korean": 0,
                    "Greek": 0,
                    "Persian/Iranian": 0,
                    "Indian": 0,
                    "Canadian": 0,
                    "Mexican": 0,
                    "American": 0,
                    "Italian": 0,
                    "Asian Fusion": 0,
                    "French": 0,
                    "Others": 0
                }
        
        for row in yelp_data:
            if row[4] == city and 'Restaurants' in row[12]:
                # If no key category exists 
                category_checked = True
                # Count the Categoies from the dataset 
                for category in restaurant_dict.keys():
                    if (category in row[12]):
                        restaurant_dict[category] += 1
                        category_checked = False 
                    if (category == "Others" and category_checked):
                        restaurant_dict[category] += 1

        sortedList = sorted(restaurant_dict.items(), key=lambda item: item[1], reverse=True)
        return sortedList
        
#  Combine the rest of the code
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
        
        dict = (restaurantCategoryDist(data_file, city))



if __name__ == "__main__":
    main()