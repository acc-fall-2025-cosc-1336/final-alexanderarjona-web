#write functions here, don't add input('') statements here!
def test_config():
    return True

def create_multiplication_table():
    table = []
    # Create rows for 1 to 5
    for i in range(1, 6):
        row = []
        # Create columns for 1 to 10
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        for num in row:
            # Print number with a little padding (4 spaces) for alignment
            print(f"{num:<4}", end="")
        print() # New line after each row

if __name__ == "__main__":
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)
        
        choice = input("\nDo you want to quit? (y/n): ")
        if choice.lower() == 'y':
            break