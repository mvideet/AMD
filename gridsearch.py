import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import f1_score

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

import numpy as np
from imblearn.over_sampling import SMOTE

df = pd.read_csv("aak81Dataset_cpmdat-1.csv")
X = df.iloc[:,1:-1]
y = df.iloc[:,-1]
le = LabelEncoder()
le.fit(y)
y = le.transform(y)
f1_array = []
for i in range(100):

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=i)
    print("finished splitting")
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 10, 20],
        'min_samples_split': [2, 5, 10]
    }
    print("finished sampling")
    rf = RandomForestClassifier(random_state=42)
    grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='f1')
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    print("finishing hpt")
    y_pred = best_model.predict(X_val)
    val_accuracy = f1_score(y_val, y_pred)
    print(val_accuracy)
    f1_array.append(val_accuracy)
print(f1_array)
pd.DataFrame(f1_array).to_csv("f1.csv")
