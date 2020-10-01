
# Define a print deliveries function
def print_deliveries(day_num, file_path):
    print(f"Day {day_num}") # prints delivery day
    the_file = open(file_path) # opens the file 
    for line in the_file:
        line = line.rstrip() # strips trailing white space for each line
        words = line.split('|') # tokenizes the line with '|' as the deliminator

        melon = words[0] # defines melon var as the first item in the words list
        count = words[1] # defines count var as the second item in the words list
        amount = words[2] # defines amount var as the third item in the words list

        print(f"Delivered {count} {melon}s for total of ${amount}") # prints statement consolidating information from the file
    the_file.close() # closes file

# For day 1 deliveries
print_deliveries(1, "um-deliveries-20140519.txt") # runs function for first day
print_deliveries(2, "um-deliveries-20140520.txt") # runs function for second day
print_deliveries(3, "um-deliveries-20140521.txt") # runs function for third day