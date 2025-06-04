def main():
    size = int(input("Enter the size of the pattern: "))
    
    # Initialize row counter
    row = 0
    
    # Outer while loop for rows
    while row < size:
        # Inner for loop to print stars in a row
        for col in range(size):
            print("*", end="")  # print * without newline
        
        print()  # print newline after each row
        row += 1  # increment row counter

if __name__ == "__main__":
    main()
