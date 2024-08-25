#YOu have a shopping list which you nee
#Menu driven coding 
def shopping_list():
    # Create an empty dictionary to store the shopping list
    shopping_dict = {}

    while True:
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View shopping list")
        print("4. Clear shopping list")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            item = input("Enter the item you want to add: ")
            quantity = int(input("Enter the quantity: "))
            shopping_dict[item] = shopping_dict.get(item, 0) + quantity
            print(f"{quantity} {item}(s) added to the shopping list.")

        elif choice == "2":
            item = input("Enter the item you want to remove: ")
            if item in shopping_dict:
                quantity = int(input(f"Enter the quantity of {item} to remove: "))
                if shopping_dict[item] >= quantity:
                    shopping_dict[item] -= quantity
                    print(f"{quantity} {item}(s) removed from the shopping list.")
                    if shopping_dict[item] == 0:
                        del shopping_dict[item]
                else:
                    print(f"Error: Not enough {item} in the shopping list.")
            else:
                print(f"{item} is not in the shopping list.")

        elif choice == "3":
            print("\nShopping List:")
            for item, quantity in shopping_dict.items():
                print(f"{item}: {quantity}")

        elif choice == "4":
            shopping_dict.clear()
            print("Shopping list cleared.")

        elif choice == "5":
            print("Thank you for using the shopping list. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4/5).")

# if __name__ == "__main__":
print(shopping_list())



#Q2  Given array will check summation of 3 elements at a time & find out the maximimum sum.
A = [35,42,35,97,66,107,121,83]
Output = [311]   #sumaation of 107,121,83


A = [35, 42, 35, 97, 66, 107, 121, 83]

# Sort the array in descending order to make it easier to find the maximum sum
A.sort(reverse=True)

# Initialize variables to store the maximum sum and the current sum
max_sum = float('-inf')
current_sum = 0

# Iterate through the sorted array and sum every 3 elements
for i in range(0, len(A) - 2, 3):
    current_sum = A[i] + A[i + 1] + A[i + 2]
    max_sum = max(max_sum, current_sum)

# Print the maximum sum
print([max_sum])
