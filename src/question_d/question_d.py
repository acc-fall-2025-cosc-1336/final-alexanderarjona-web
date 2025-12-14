#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    len1 = len(dna_string1)
    len2 = len(dna_string2)

    # Loop through string 1 to find occurrences of string 2
    for i in range(len1 - len2 + 1):
        # Check if the slice matches the substring
        if dna_string1[i : i + len2] == dna_string2:
            # Add 1 to index because the problem asks for 1-based positions
            positions.append(i + 1)
            
    # Return as multiple values (tuple)
    return tuple(positions)

if __name__ == "__main__":
    while True:
        # Validation Loop
        while True:
            s = input("Enter DNA string (8-16 chars): ").upper()
            t = input("Enter DNA substring (exactly 4 chars): ").upper()

            if 8 < len(s) <= 16 and len(t) == 4:
                break
            else:
                print("Invalid input. String must be 9-16 chars and substring 4 chars.")

        # Call function and get result
        result = get_most_likely_ancestor_consensus(s, t)
        
        # Display the tuple result unpacked as space-separated values
        print(*result)

        choice = input("\nDo you want to quit? (y/n): ")
        if choice.lower() == 'y':
            break