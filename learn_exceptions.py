import csv

def get_col_sum(file, col):
    
    csv_file = open(file)
    
    csv_reader = csv.reader(csv_file)
    
    running_sum = 0
    
    # Learning:
    #     try
    #     /   \
    #  except else
    #    \    /
    #   finally
    for row in csv_reader:
        try:
            if int(row[col]):
                running_sum += int(row[col])
            elif float(row[col]):
                running_sum += float(row[col])
        except Exception:
            # Not a valid number
            print(f"{row[col]} is not a number")
            continue
        #else: # when you don't enter the exception block
    print(running_sum)
    csv_file.close()
    
    
if __name__ == '__main__':
    get_col_sum('./data/test_csv.csv', 3)