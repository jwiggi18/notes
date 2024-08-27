import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the data
df = pd.read_csv('sample_data.csv')

# 1. Data Cleaning
# Handle missing values
numeric_features = ['age', 'income']
categorical_features = ['education', 'occupation']

# Create preprocessing pipelines
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Remove duplicates
df.drop_duplicates(inplace=True)

# 2. Data Transformation
# Note: Normalization/Standardization is handled in the pipeline above

# 3. Feature Engineering
# Create a new feature
df['income_per_age'] = df['income'] / df['age']

# 4. Handle Outliers
# Example: Capping outliers in 'income' column
Q1 = df['income'].quantile(0.25)
Q3 = df['income'].quantile(0.75)
IQR = Q3 - Q1
df['income'] = df['income'].clip(lower=Q1 - 1.5*IQR, upper=Q3 + 1.5*IQR)

# 5. Data Type Conversion
# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# 6. Handle Imbalanced Data
# Note: This step depends on your specific dataset and problem

# 7. Data Anonymization
# Example: Removing a sensitive column
df.drop('ssn', axis=1, inplace=True, errors='ignore')

# 8. Data Validation
# Example: Check for any remaining missing values
print("Remaining missing values:\n", df.isnull().sum())

# 9. Data Partitioning
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply preprocessing
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# 10. Document Preprocessing Steps
print("Preprocessing steps:")
print(preprocessor.named_transformers_['num'].named_steps['imputer'])
print(preprocessor.named_transformers_['cat'].named_steps['onehot'])

# The preprocessed data is now ready for modeling
print("Shape of processed training data:", X_train_processed.shape)
print("Shape of processed test data:", X_test_processed.shape)
