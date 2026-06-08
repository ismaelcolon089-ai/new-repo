# Standard Deviation Lab

This project demonstrates how to calculate the **population standard deviation** for the dataset provided in the assignment.

## Dataset
The number of books read by eight learners in one month:

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

## Step-by-step calculation
1. **Mean**
   - `(2 + 4 + 4 + 4 + 5 + 5 + 7 + 9) / 8 = 40 / 8 = 5`

2. **Squared differences from the mean**
   - `(2 - 5)² = 9`
   - `(4 - 5)² = 1`
   - `(4 - 5)² = 1`
   - `(4 - 5)² = 1`
   - `(5 - 5)² = 0`
   - `(5 - 5)² = 0`
   - `(7 - 5)² = 4`
   - `(9 - 5)² = 16`

3. **Variance**
   - `(9 + 1 + 1 + 1 + 0 + 0 + 4 + 16) / 8 = 32 / 8 = 4`

4. **Standard deviation**
   - `√4 = 2`

## Result
The standard deviation of the dataset is **2**.

This means that, on average, the number of books read differs from the mean by **2 books**.

## Project files
- `standard_deviation.py` — Python script that calculates the mean, variance, and standard deviation
- `newfile.txt` — original tracked file from the repo history

## How to run
If Python is installed, run:

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
