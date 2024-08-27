import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the data
df = pd.read_csv('sample_data.csv')

# 1. Initial Data Overview
def initial_overview(df):
    print("Dataset shape:", df.shape)
    print("\nColumn info:")
    print(df.info())
    print("\nBasic statistics:")
    print(df.describe())
    print("\nMissing values:")
    print(df.isnull().sum())

initial_overview(df)

# 2. Univariate Analysis
def univariate_analysis(df, numeric_col, categorical_col):
    # Numeric variable
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    df[numeric_col].hist()
    plt.title(f'Histogram of {numeric_col}')
    plt.subplot(132)
    stats.probplot(df[numeric_col], dist="norm", plot=plt)
    plt.title("Q-Q plot")
    plt.subplot(133)
    sns.boxplot(y=df[numeric_col])
    plt.title('Box plot')
    plt.tight_layout()
    plt.show()

    # Categorical variable
    plt.figure(figsize=(10, 5))
    df[categorical_col].value_counts().plot(kind='bar')
    plt.title(f'Bar plot of {categorical_col}')
    plt.show()

univariate_analysis(df, 'age', 'education')

# 3. Bivariate Analysis
def bivariate_analysis(df, numeric_col1, numeric_col2, categorical_col):
    # Numeric vs Numeric
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=numeric_col1, y=numeric_col2)
    plt.title(f'Scatter plot: {numeric_col1} vs {numeric_col2}')
    plt.show()

    # Numeric vs Categorical
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=categorical_col, y=numeric_col1)
    plt.title(f'Box plot: {categorical_col} vs {numeric_col1}')
    plt.xticks(rotation=45)
    plt.show()

bivariate_analysis(df, 'age', 'income', 'education')

# 4. Multivariate Analysis
def multivariate_analysis(df):
    # Correlation matrix
    corr = df.select_dtypes(include=[np.number]).corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

    # Pair plot
    sns.pairplot(df, hue='education')
    plt.show()

multivariate_analysis(df)

# 5. Time Series Analysis (if applicable)
def time_series_analysis(df, date_col, value_col):
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col)
    df[value_col].plot(figsize=(12, 6))
    plt.title(f'Time Series of {value_col}')
    plt.show()

# Uncomment and use if you have time series data
# time_series_analysis(df, 'date', 'sales')

# 6. Advanced Visualization
def advanced_visualization(df):
    # Interactive scatter plot
    fig = px.scatter(df, x='age', y='income', color='education', hover_data=['occupation'])
    fig.show()

    # PCA visualization
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    scaler = StandardScaler()
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaler.fit_transform(df[numeric_cols]))
    df['pca-one'] = pca_result[:,0]
    df['pca-two'] = pca_result[:,1] 
    plt.figure(figsize=(10,8))
    sns.scatterplot(x="pca-one", y="pca-two", hue="education", data=df)
    plt.title('PCA visualization')
    plt.show()

advanced_visualization(df)

# 7. Statistical Tests
def statistical_tests(df, numeric_col, categorical_col):
    # Normality test
    stat, p = stats.normaltest(df[numeric_col])
    print(f"Normality test for {numeric_col}:")
    print(f"Statistics={stat:.3f}, p={p:.3f}")

    # ANOVA test
    categories = df[categorical_col].unique()
    anova_results = stats.f_oneway(*[df[df[categorical_col] == cat][numeric_col] for cat in categories])
    print(f"\nANOVA test for {numeric_col} across {categorical_col} categories:")
    print(f"F-statistic={anova_results.statistic:.3f}, p={anova_results.pvalue:.3f}")

statistical_tests(df, 'income', 'education')

# Run all analyses
if __name__ == "__main__":
    initial_overview(df)
    univariate_analysis(df, 'age', 'education')
    bivariate_analysis(df, 'age', 'income', 'education')
    multivariate_analysis(df)
    advanced_visualization(df)
    statistical_tests(df, 'income', 'education')
