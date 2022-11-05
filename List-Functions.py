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

print("\nWelcome aboard! In this program, you have an array containing 10 random numbers. Check the menu below to know what features this program has to offer.")
array = [3, 8, 45, 21, 1, 78, 301, 59, 9, 0]
print(f"\nYour array: {array}")

print("\nMenu: \n1 -> Add an element \n2 -> Insert an element \n3 -> Modify an element \n4 -> Delete an element \n5 -> Arrange in ascending order \n6 -> Arrange in descending order \n7 -> Double check the length \n8 -> Count an element \n9 -> Find the index of an element \n10 -> Pop an element")

# desiredFunc = False

# while not desiredFunc:
#     desiredFunc = int(input("\nWhat do you want to do? (1-6): "))
#     if desiredFunc > 1 and desiredFunc < 6:
#         break
#     else:
#         print("\nThe number you entered is beyond the scope of this program. Try choosing from 1 to 6.")

desiredFunc = int(input("\nWhat do you want to do? (1-10): "))

if desiredFunc == 1:
    desiredNum = int(input("Enter the number you want to add: "))
    array.append(desiredNum)
    print(f"\nThis is your new array: {array}\n")

elif desiredFunc == 2:
    desiredNum = int(input("Enter the number you want to insert: "))
    desiredIndex = int(input("Enter the index you want to insert the number: "))
    array.insert(desiredIndex, desiredNum)
    print(f"\nThis is your new array: {array}\n")

elif desiredFunc == 3:
    desiredNum = int(input("Enter the number you want to modify: "))
    desiredIndex = int(input("Enter the index you want to modify: "))
    array[desiredIndex] = desiredNum
    print(f"\nThis is your new array: {array}\n")

elif desiredFunc == 4:
    desiredNum = int(input("Enter the number you want to remove: "))
    array.remove(desiredNum)
    print(f"\nThis is your new array: {array}\n")

elif desiredFunc == 5:
    array.sort()
    print(f"\nThis is your new array: {array}\n")

elif desiredFunc == 6:
    array.sort(reverse=True)
    print(f"\nThis is your new array: {array}\n")

elif desiredFunc == 7:
    print(f"\nThe length of the array is {len(array)}\n")

elif desiredFunc == 8:
    desiredNum = int(input("Enter the number you want to count: "))
    if desiredNum >= 1 and desiredNum <= 10:
        counter = array.count(desiredNum)
        print(f"\nThe number {desiredNum} is repeated {counter} time/s in the array.\n")
    else:
        print(f"\nThe array does not contain the number {desiredNum}.\n")

elif desiredFunc == 9:
    desiredNum = int(input("Enter the number you want to know the index of: "))
    if desiredNum in array:
        index = array.index(desiredNum)
        print(f"\nThe number {desiredNum} has an index of {index}.\n")
    else:
        print(f"\nThe array does not contain the number {desiredNum}.\n")

elif desiredFunc == 10:
    desiredIndex = int(input("Enter the index of the number you want to pop: "))
    print(f"\nHere's the number you popped: {array[desiredIndex]}")
    array.pop(desiredIndex)
    print(f"This is your new array: {array}\n")