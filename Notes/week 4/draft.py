import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame for Week 1
data_week1 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
              'Age': [25, 30, 35, 40],
              'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df_week1 = pd.DataFrame(data_week1)

# Sample DataFrame for Week 2
data_week2 = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
              'Age': [25, 30, 35, 40, 28, 45],
              'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Los Angeles', 'New York'],
              'Value': [10, 20, 15, 25, 30, 35],
              'Date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01']),
              'Income': [50000, 60000, 75000, 80000, 70000, 90000],
              'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'PhD']}
df = pd.DataFrame(data_week2)

# Use df_week2 for Week 3 examples

# Plotting a column
df['Age'].plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
