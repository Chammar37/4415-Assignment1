import csv

def drawEdges(data_file):
    with open(data_file, 'r', encoding='utf8') as business:
        yelp_data = csv.reader(business, delimiter=",")
    
    for row in yelp_data:
        spliting_row = row[4].split(",")
        







def main():
    drawEdges()



if __name__ == "__main__":
    main()