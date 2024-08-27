import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the data
df = pd.read_csv('sample_data.csv')

# 1. Data Profiling
def profile_data(df):
    print("Data Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nBasic Statistics:")
    print(df.describe())

profile_data(df)

# 2. Completeness Check
def check_completeness(df):
    missing_data = df.isnull().sum()
    missing_percent = 100 * df.isnull().sum() / len(df)
    missing_table = pd.concat([missing_data, missing_percent], axis=1, keys=['Total Missing', 'Percent Missing'])
    print("\nMissing Data:")
    print(missing_table)

    # Visualize missing data
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
    plt.title('Missing Data Heatmap')
    plt.tight_layout()
    plt.show()

check_completeness(df)

# 3. Consistency and Validity Checks
def check_consistency(df):
    print("\nDuplicate Rows:", df.duplicated().sum())
    
    # Example: Check if 'age' is within a valid range
    invalid_age = df[(df['age'] < 0) | (df['age'] > 120)].shape[0]
    print("Invalid age entries:", invalid_age)

check_consistency(df)

# 4. Outlier Detection
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"\nOutliers in {column}:", outliers.shape[0])

    # Visualize outliers
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot of {column}')
    plt.show()

detect_outliers(df, 'salary')

# 5. Data Type Verification
def verify_data_types(df):
    print("\nCurrent Data Types:")
    print(df.dtypes)
    
    # Example: Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    print("\nUpdated 'date' column type:", df['date'].dtype)

verify_data_types(df)

# 6. Uniqueness and Cardinality Analysis
def analyze_cardinality(df):
    for column in df.select_dtypes(include=['object']):
        unique_count = df[column].nunique()
        print(f"\nUnique values in {column}: {unique_count}")
        if unique_count < 10:  # For low cardinality columns
            print(df[column].value_counts())

analyze_cardinality(df)

# 7. Data Distribution Analysis
def analyze_distribution(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

    # Normality test
    _, p_value = stats.normaltest(df[column].dropna())
    print(f"\nNormality test p-value for {column}: {p_value}")
    if p_value < 0.05:
        print(f"The {column} distribution is likely not normal.")
    else:
        print(f"The {column} distribution is likely normal.")

analyze_distribution(df, 'salary')

# Main execution
if __name__ == "__main__":
    profile_data(df)
    check_completeness(df)
    check_consistency(df)
    detect_outliers(df, 'salary')
    verify_data_types(df)
    analyze_cardinality(df)
    analyze_distribution(df, 'salary')
