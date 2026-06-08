import math

# Custom dataset for Assessment 1
books_read = [8, 8, 8, 8, 12, 12, 12, 12]

# Step 1: Calculate the mean (average)
mean_books = sum(books_read) / len(books_read)

# Step 2: Calculate the deviations from the mean
deviations = [value - mean_books for value in books_read]

# Step 3: Square each deviation
squared_differences = [value ** 2 for value in deviations]

# Step 4: Calculate the variance
variance = sum(squared_differences) / len(books_read)

# Step 5: Take the square root of the variance to get the standard deviation
standard_deviation = math.sqrt(variance)

print("Standard Deviation Lab")
print(f"Dataset: {books_read}")
print(f"Mean: {mean_books}")
print(f"Deviations from the mean: {deviations}")
print(f"Squared differences: {squared_differences}")
print(f"Variance: {variance}")
print(f"Standard deviation: {standard_deviation}")
