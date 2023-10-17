# Pandas 

## Basic

### `Series` & `DataFrame`

- `pandas` installation

```python
pip install pandas

import pandas as pd
```

- `Series`: 1-D 배열같은 object, 리스트랑 비슷함 (콤마로 요소 구분)

```python
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(data)
```

- `DataFrame`: 2-D 데이터 스트럭쳐 w/ 레이블 (행렬)
- 리스트, 딕셔너리, 넘파이 배열 등으로 만들수 있음
- 보통 `df`로 많이 사용

```python
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
```

- Basic `DataFrame` Operations
- Viewing Data (데이터 확인)

```python
# Display the first few rows of the DataFrame
print(df.head())

# Display the last few rows of the DataFrame
print(df.tail())
```

- Accessing Columns (특정 열 접근)

```python
# Access a single column
print(df['Name'])

# Access multiple columns
print(df[['Name', 'Age']])
```

- Descriptive Statistics (통계적 정보)

```python
# Get summary statistics of the DataFrame
print(df.describe())
```

### Read & Write CSV w/ `pandas`

- Reading CSV

```python
# Read a CSV file into a DataFrame
file_path = 'your_file.csv'
df = pd.read_csv(file_path)
```

- Writing CSV

```python
# Write DataFrame to a CSV file
df.to_csv('output_file.csv', index=False)
```

### Indexing and Selection

- Selecting Rows

```python
# Selecting a single row by index
row_1 = df.loc[0]

# Selecting multiple rows by index
rows_1_and_2 = df.loc[[0, 1]]

# Selecting rows based on a condition
young_people = df[df['Age'] < 30]
```

- Selecting Columns

```python
# Selecting a single column
name_column = df['Name']

# Selecting multiple columns
name_and_age = df[['Name', 'Age']]
```

### Data Cleaning and Handling Missing Values

- Checking for Missing Values

```python
# Check for missing values in the entire DataFrame
print(df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value
df_filled = df.fillna(value=0)
```

- Removing Duplicates

```python
# Remove duplicate rows based on all columns
df_no_duplicates = df.drop_duplicates()

# Remove duplicate rows based on specific columns
df_no_duplicates_name = df.drop_duplicates(subset=['Name'])
```

### Grouping and Aggregation

- Grouping Data

```python
# Grouping data by a column
grouped_by_city = df.groupby('City')

# Applying aggregation functions
average_age_by_city = grouped_by_city['Age'].mean()
```

- Merging DataFrames

```python
# Creating a second DataFrame
data2 = {'Name': ['Eva', 'Frank'],
         'Age': [28, 45],
         'City': ['Los Angeles', 'New York']}
df2 = pd.DataFrame(data2)

# Merging DataFrames
merged_df = pd.concat([df, df2], ignore_index=True)
```

### Time Series Data

- Working with Dates

```python
# Convert a column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extracting date components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
```

- Resampling Time Series Data

```python
# Resample time series data (e.g., monthly mean)
df_resampled = df.resample('M').mean()
```