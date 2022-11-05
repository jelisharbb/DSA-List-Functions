# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array

# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:
# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

array = [3, 8, 45, 21, 1, 78, 301, 59, 9, 0]
print(array)

print("\nMenu: \n1 -> Add an element \n2 -> Insert an element \n3 -> Modify an element \n4 -> Delete an element \n5 -> Arrange in ascending order \n6 -> Arrange in descending order")

desiredFunc = int(input("\nWhat do you want to do? (1-6): "))

if desiredFunc == 1:
    desiredNum = int(input("Enter the number you want to add: "))
    array.append(desiredNum)
    print(f"\nThis is your new array: {array} ")

elif desiredFunc == 2:
    desiredNum = int(input("Enter the number you want to insert: "))
    desiredIndex = int(input("Enter the index you want to insert the number: "))
    array.insert(desiredIndex, desiredNum)
    print(f"\nThis is your new array: {array} ")

elif desiredFunc == 3:
    desiredNum = int(input("Enter the number you want to modify: "))
    desiredIndex = int(input("Enter the index you want to modify: "))
    array[desiredIndex] = desiredNum
    print(f"\nThis is your new array: {array} ")