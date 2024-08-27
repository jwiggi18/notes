import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the data
df = pd.read_csv('sample_data.csv')

# 1. Feature Creation
def create_features(df):
    # Arithmetic combination
    df['bmi'] = df['weight'] / (df['height'] / 100) ** 2
    
    # Aggregation
    df['total_debt'] = df['credit_card_debt'] + df['mortgage_debt'] + df['personal_loan']
    
    # Binning
    df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 65, 100], labels=['0-18', '19-35', '36-50', '51-65', '65+'])
    
    # Extraction from datetime
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['transaction_year'] = df['transaction_date'].dt.year
    df['transaction_month'] = df['transaction_date'].dt.month
    df['transaction_day'] = df['transaction_date'].dt.day
    
    return df

df = create_features(df)

# 2. Feature Transformation
numeric_features = ['age', 'income', 'bmi', 'total_debt']
categorical_features = ['education', 'occupation', 'age_group']

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

# 3. Feature Selection
def select_features(X, y, k=5):
    selector = SelectKBest(score_func=f_classif, k=k)
    X_selected = selector.fit_transform(X, y)
    selected_feature_indices = selector.get_support(indices=True)
    selected_features = X.columns[selected_feature_indices]
    return X_selected, selected_features

# 4. Dimensionality Reduction
def apply_pca(X, n_components=2):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    return X_pca, pca

# 5. Interaction Features
def create_interaction_features(df):
    df['income_per_age'] = df['income'] / df['age']
    return df

df = create_interaction_features(df)

# 6. Time-based Features (assuming 'transaction_date' is a datetime column)
def create_time_features(df):
    df['days_since_last_transaction'] = (pd.Timestamp.now() - df['transaction_date']).dt.days
    df['is_weekend'] = df['transaction_date'].dt.dayofweek.isin([5, 6]).astype(int)
    return df

df = create_time_features(df)

# Main execution
if __name__ == "__main__":
    # Prepare the data
    X = df.drop('target', axis=1)  # Assuming 'target' is your target variable
    y = df['target']
    
    # Apply preprocessing
    X_preprocessed = preprocessor.fit_transform(X)
    
    # Feature selection
    X_selected, selected_features = select_features(X_preprocessed, y)
    print("Selected features:", selected_features)
    
    # Apply PCA
    X_pca, pca = apply_pca(X_selected)
    print("Explained variance ratio:", pca.explained_variance_ratio_)
    
    # The final feature set is now ready for modeling
    print("Final feature set shape:", X_pca.shape)
