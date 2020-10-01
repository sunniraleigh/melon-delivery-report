
# Define a print deliveries function
def print_deliveries(day_num, file_path):
    print(f"Day {day_num}")
    the_file = open(file_path)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

# For day 1 deliveries
print_deliveries(1, "um-deliveries-20140519.txt")
print_deliveries(2, "um-deliveries-20140520.txt")
print_deliveries(3, "um-deliveries-20140521.txt")