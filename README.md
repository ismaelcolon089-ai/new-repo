# Standard Deviation Lab

This project shows the steps used to calculate the standard deviation for the dataset in the assignment.

## Dataset
`2, 4, 4, 4, 5, 5, 7, 9`

## Objective
By the end of this lab, learners will be able to calculate the standard deviation.

## Formula used
Population standard deviation:

`σ = √(Σ(x - μ)² / N)`

Where:
- `μ` = mean
- `N` = number of data points
- `x` = each value in the dataset

## Here are the steps to calculate the standard deviation

1. **Calculate the mean (average) of the data set:**
   - `X̄ = (2 + 4 + 4 + 4 + 5 + 5 + 7 + 9) / 8`
   - `X̄ = 40 / 8 = 5`

2. **Calculate the squared differences from the mean for each data point:**
   - `(2 - 5)² = (-3)² = 9`
   - `(4 - 5)² = (-1)² = 1`
   - `(4 - 5)² = (-1)² = 1`
   - `(4 - 5)² = (-1)² = 1`
   - `(5 - 5)² = 0² = 0`
   - `(5 - 5)² = 0² = 0`
   - `(7 - 5)² = 2² = 4`
   - `(9 - 5)² = 4² = 16`

3. **Calculate the average of these squared differences (variance):**
   - `Variance = (9 + 1 + 1 + 1 + 0 + 0 + 4 + 16) / 8`
   - `Variance = 32 / 8 = 4`

4. **Take the square root of the variance to get the standard deviation:**
   - `√4 = 2`

## Result
The standard deviation of the dataset is **2**.

## Project files
- `standard_deviation.py` — Python script with comments that calculates the mean, variance, and standard deviation
- `newfile.txt` — original tracked file from the repo history

## How to run
```bash
python standard_deviation.py
```

## Expected output
```text
Standard Deviation Lab
Dataset: [2, 4, 4, 4, 5, 5, 7, 9]
Mean: 5.0
Squared differences: [9.0, 1.0, 1.0, 1.0, 0.0, 0.0, 4.0, 16.0]
Variance: 4.0
Standard deviation: 2.0
```
