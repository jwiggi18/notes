import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('sample_data.csv')

# 1. Data Preparation
X = df.drop('target', axis=1)
y = df['target']

# 2. Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Define models
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

# 4. Model Selection and Cross-Validation
def evaluate_models(models, X, y):
    results = []
    for name, model in models.items():
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', model)
        ])
        scores = cross_val_score(pipeline, X, y, cv=5, scoring='accuracy')
        results.append({
            'model': name,
            'mean_score': np.mean(scores),
            'std_score': np.std(scores)
        })
    return pd.DataFrame(results)

results = evaluate_models(models, X_train, y_train)
print(results)

# Visualize model performance
plt.figure(figsize=(10, 6))
sns.barplot(x='model', y='mean_score', data=results)
plt.title('Model Performance Comparison')
plt.ylim(0.5, 1)
plt.show()

# 5. Hyperparameter Tuning (example with Random Forest)
rf_params = {
    'model__n_estimators': [100, 200, 300],
    'model__max_depth': [None, 5, 10],
    'model__min_samples_split': [2, 5, 10]
}

rf_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])

grid_search = GridSearchCV(rf_pipeline, rf_params, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best cross-validation score:", grid_search.best_score_)

# 6. Final Model Training and Evaluation
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

y_pred = best_model.predict(X_test)
print("Test set accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. Feature Importance (for Random Forest)
feature_importance = best_model.named_steps['model'].feature_importances_
feature_importance_df = pd.DataFrame({
    'feature': X.columns,
    'importance': feature_importance
}).sort_values('importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='importance', y='feature', data=feature_importance_df.head(10))
plt.title('Top 10 Feature Importances')
plt.show()

# 8. Model Persistence
import joblib

joblib.dump(best_model, 'best_model.joblib')

print("Model saved as 'best_model.joblib'")
