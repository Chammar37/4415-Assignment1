import csv
import sys
import matplotlib.pyplot as plt

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

    return dict(sorted(restaurant_dict.items(), key=lambda item: item[1], reverse=True))

def restaurantReviewDist (data_file, city):
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
                        restaurant_dict[key][0] += int(row[10])
                        restaurant_dict[key][1] += float(row[9])

                    else:
                        restaurant_dict[key] = [int(row[10]), float(row[9])]

        # Finding Average of the stars
        star_counter_list = restaurantCategoryDist(data_file, city)
        for key in restaurant_dict.keys():
            restaurant_dict[key][1] = restaurant_dict[key][1] / star_counter_list[key]

    return dict(sorted(restaurant_dict.items(), key=lambda item: item[1], reverse=True))


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

        # print category
        print("\ncategory:#restaurants")

        category_dict = list(restaurantCategoryDist(data_file, city).items())[:10]
        category = []
        category_counter = []

        for key in category_dict:
            category.append(key[0])
            category_counter.append(key[1])
            print(key[0] + ":" + str(key[1]))

        #print review
        print("\ncategory:#reviews:avg_stars")
        review_dict = list(restaurantReviewDist(data_file,city).items())[:10]
        
        for key in review_dict:
            print(key[0] + ":" + str(key[1][0]) + ":"+ str("{:.1f}".format(key[1][1])))

         # Draw the Bar Graph
        plt.figure(figsize=(16, 5))
        plt.bar(category,category_counter)
        plt.title("Restaurant Category Distribution")
        plt.xlabel("Categories")
        plt.ylabel("Number of Restaurant")
        plt.show()

if __name__ == "__main__":
    main()