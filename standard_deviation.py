"""
Standard Deviation Lab

This script demonstrates how to calculate the population standard deviation
for the dataset provided in the assignment.
"""

import math

# Dataset: number of books read by eight learners in one month.
data = [2, 4, 4, 4, 5, 5, 7, 9]

# Step 1: Calculate the mean (average).
mean = sum(data) / len(data)

# Step 2: Calculate each squared difference from the mean.
squared_differences = [(value - mean) ** 2 for value in data]

# Step 3: Calculate the variance by averaging the squared differences.
variance = sum(squared_differences) / len(data)

# Step 4: Take the square root of the variance to get the standard deviation.
standard_deviation = math.sqrt(variance)

print("Standard Deviation Lab")
print(f"Dataset: {data}")
print(f"Mean: {mean}")
print(f"Squared differences: {squared_differences}")
print(f"Variance: {variance}")
print(f"Standard deviation: {standard_deviation}")
