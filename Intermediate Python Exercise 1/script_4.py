total = 0
# Loop and range being set
for i in range(1,6):
    while True:
        try:
            # Prompt user to input an integer
            user_int = int(input("Enter int #{}: ".format(i)))
            total += user_int
            break
        except ValueError:
            # Prompt user to re-input an integer
            print("Invalid input. Please enter a int.")
            continue

# Use print method to print the total        
print("Your sum is",total)
