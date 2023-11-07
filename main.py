# Computation.py - This program calculates sum, difference, and product of two values.
# Input: Interactive
# Output: Sum, difference, and product of two values.

# Write calculateSum function here
def calculateSum(x, y):
    a = x + y
    return a


# Write calculateDifference function here
def calculateDifference(x, y):
    a = x - y
    return a


# Write calculateProduct function here
def calculateProduct(x, y):
    a = x * y
    return a


value1 = int(input("Enter first numeric value: "))
value2 = int(input("Enter second numeric value: "))

# Call calculateSum
print("The Sum of the given values is: ", calculateSum(value1, value2))
# Call calculateDifference
print("The Difference between the given values is: ", calculateDifference(value1, value2))

# Call calculateProduct
print("The Difference between the given values is: ", calculateProduct(value1, value2))
