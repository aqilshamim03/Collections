# Creating a list
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Accessing elements
print("First element:", my_list[0])   # index starts at 0
print("Last element:", my_list[-1])  # negative index means from end


fruits = ["apple", "banana", "cherry"]

# Add elements
fruits.append("mango")       # adds at end
fruits.insert(1, "orange")   # insert at index 1
print("After adding:", fruits)

# Remove elements
fruits.remove("banana")      # removes "banana"
popped = fruits.pop()        # removes last element
print("After removing:", fruits)
print("Popped element:", popped)


nums = [3, 1, 4, 1, 5, 9]

print("Length:", len(nums))     # number of elements
print("Sorted:", sorted(nums))  # returns sorted copy
nums.sort()                     # sorts in place
print("Sorted in place:", nums)
print("Count of 1:", nums.count(1)) # how many times 1 appears
print("Index of 5:", nums.index(5)) # first position of 5
