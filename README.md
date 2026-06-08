# Statistics Lab Portfolio

This repository now contains both assessments completed with original datasets while following the formulas and process shown in the assignments.

## Assessment 1: Standard Deviation

### Custom Dataset
`8, 8, 8, 8, 12, 12, 12, 12`

### Step 1: Calculate the Mean
- `(8 + 8 + 8 + 8 + 12 + 12 + 12 + 12) / 8`
- `80 / 8 = 10`

### Step 2: Calculate the Deviations from the Mean
- `8 - 10 = -2`
- `8 - 10 = -2`
- `8 - 10 = -2`
- `8 - 10 = -2`
- `12 - 10 = 2`
- `12 - 10 = 2`
- `12 - 10 = 2`
- `12 - 10 = 2`

### Step 3: Square Each Deviation
- `(-2)^2 = 4`
- `(-2)^2 = 4`
- `(-2)^2 = 4`
- `(-2)^2 = 4`
- `(2)^2 = 4`
- `(2)^2 = 4`
- `(2)^2 = 4`
- `(2)^2 = 4`

### Step 4: Calculate the Variance
- `(4 + 4 + 4 + 4 + 4 + 4 + 4 + 4) / 8`
- `32 / 8 = 4`

### Step 5: Calculate the Standard Deviation
- `√4 = 2`

### Result
The standard deviation of the dataset is **2**.

---

## Assessment 2: Covariance and Correlation

### Custom Dataset
- Day 1: Temperature = `18`, Ice Cream Sales = `90`
- Day 2: Temperature = `22`, Ice Cream Sales = `110`
- Day 3: Temperature = `26`, Ice Cream Sales = `130`

### Step 1: Calculate the Means
- Mean temperature: `(18 + 22 + 26) / 3 = 66 / 3 = 22`
- Mean sales: `(90 + 110 + 130) / 3 = 330 / 3 = 110`

### Step 2: Calculate Deviations from the Mean
#### Temperature Deviations
- `18 - 22 = -4`
- `22 - 22 = 0`
- `26 - 22 = 4`

#### Ice Cream Sales Deviations
- `90 - 110 = -20`
- `110 - 110 = 0`
- `130 - 110 = 20`

### Step 3: Multiply Deviations and Calculate Covariance
- `(-4) × (-20) = 80`
- `0 × 0 = 0`
- `4 × 20 = 80`

Sum of products:
- `80 + 0 + 80 = 160`

Covariance:
- `160 / 3 = 53.333333333333336`

This positive covariance shows that as temperature increases, ice cream sales also increase.

### Step 4: Calculate the Correlation Coefficient
#### 4.1 Square Each Deviation
Temperature squared deviations:
- `(-4)^2 = 16`
- `0^2 = 0`
- `(4)^2 = 16`

Sales squared deviations:
- `(-20)^2 = 400`
- `0^2 = 0`
- `(20)^2 = 400`

#### 4.2 Calculate the Variance
Temperature variance:
- `(16 + 0 + 16) / 3 = 32 / 3 = 10.666666666666666`

Sales variance:
- `(400 + 0 + 400) / 3 = 800 / 3 = 266.6666666666667`

#### 4.3 Calculate the Standard Deviations
- Temperature standard deviation: `√10.666666666666666 = 3.265986323710904`
- Sales standard deviation: `√266.6666666666667 = 16.32993161855452`

#### 4.4 Apply the Correlation Formula
- `r = covariance / (σx × σy)`
- `r = 53.333333333333336 / (3.265986323710904 × 16.32993161855452)`
- `r = 1.0`

### Result
The correlation coefficient is **1.0**, which means a perfect positive relationship in this custom dataset.

### Interpretation
- Positive covariance means both variables move in the same direction.
- Positive correlation means higher temperatures are associated with higher ice cream sales.
- A value of `1.0` shows a very strong positive linear relationship.

### Visualization
The graph below shows the relationship between temperature and ice cream sales.

![Temperature and Ice Cream Sales Visualization](temperature_icecream_plot.png)

---

## Files
- `standard_deviation_lab.py` — Assessment 1 Python script
- `covariance_correlation_lab.py` — Assessment 2 Python script
- `temperature_icecream_plot.png` — visualization for Assessment 2
- `requirements.txt` — Python dependency for the plot

## How to Run
1. Create a virtual environment:
```bash
python3 -m venv .venv
```

2. Install dependencies:
```bash
.venv/bin/pip install -r requirements.txt
```

3. Run Assessment 1:
```bash
.venv/bin/python standard_deviation_lab.py
```

4. Run Assessment 2:
```bash
.venv/bin/python covariance_correlation_lab.py
```
