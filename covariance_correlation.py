import math
import matplotlib.pyplot as plt

# Dataset: daily temperature (X) and ice cream sales (Y)
temperatures = [20, 25, 15]
ice_cream_sales = [100, 120, 80]
days = [1, 2, 3]

# Step 1: Calculate the means (averages)
mean_temperature = sum(temperatures) / len(temperatures)
mean_sales = sum(ice_cream_sales) / len(ice_cream_sales)

# Step 2: Calculate deviations from the mean for X and Y
temperature_deviations = [x - mean_temperature for x in temperatures]
sales_deviations = [y - mean_sales for y in ice_cream_sales]

# Step 3: Multiply deviations and calculate covariance
products_of_deviations = [
    x_dev * y_dev for x_dev, y_dev in zip(temperature_deviations, sales_deviations)
]
covariance = sum(products_of_deviations) / len(temperatures)

# Step 4.1: Square each deviation
temperature_squared_deviations = [value ** 2 for value in temperature_deviations]
sales_squared_deviations = [value ** 2 for value in sales_deviations]

# Step 4.2: Calculate variance for each variable
temperature_variance = sum(temperature_squared_deviations) / len(temperatures)
sales_variance = sum(sales_squared_deviations) / len(ice_cream_sales)

# Step 4.3: Take the square root of variance to get standard deviation
temperature_std_dev = math.sqrt(temperature_variance)
sales_std_dev = math.sqrt(sales_variance)

# Step 4.4: Calculate the correlation coefficient
correlation_coefficient = covariance / (temperature_std_dev * sales_std_dev)

# Print the full step-by-step results
print("Covariance and Correlation Lab")
print(f"Temperature data: {temperatures}")
print(f"Ice cream sales data: {ice_cream_sales}")
print(f"Mean temperature: {mean_temperature}")
print(f"Mean ice cream sales: {mean_sales}")
print(f"Temperature deviations: {temperature_deviations}")
print(f"Sales deviations: {sales_deviations}")
print(f"Products of deviations: {products_of_deviations}")
print(f"Covariance: {covariance}")
print(f"Temperature squared deviations: {temperature_squared_deviations}")
print(f"Sales squared deviations: {sales_squared_deviations}")
print(f"Temperature variance: {temperature_variance}")
print(f"Sales variance: {sales_variance}")
print(f"Temperature standard deviation: {temperature_std_dev}")
print(f"Sales standard deviation: {sales_std_dev}")
print(f"Correlation coefficient: {correlation_coefficient}")

# Create a scatter plot and trend line for the visualization
plt.figure(figsize=(8, 5))
plt.scatter(temperatures, ice_cream_sales, color="purple", s=100, label="Data points")

# Draw mean lines
plt.axvline(mean_temperature, color="blue", linestyle="--", label=f"Mean temperature = {mean_temperature}")
plt.axhline(mean_sales, color="orange", linestyle="--", label=f"Mean sales = {mean_sales}")

# Add a trend line
slope = sum(products_of_deviations) / sum(temperature_squared_deviations)
intercept = mean_sales - (slope * mean_temperature)
trend_x = [min(temperatures), max(temperatures)]
trend_y = [slope * x + intercept for x in trend_x]
plt.plot(trend_x, trend_y, color="green", label="Trend line")

# Label the points with day numbers
for day, x, y in zip(days, temperatures, ice_cream_sales):
    plt.annotate(f"Day {day}", (x, y), textcoords="offset points", xytext=(5, 5))

plt.title("Temperature vs Ice Cream Sales")
plt.xlabel("Temperature")
plt.ylabel("Ice Cream Sales")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("temperature_icecream_plot.png", dpi=200)
print("Plot saved as temperature_icecream_plot.png")
