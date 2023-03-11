from bayes_opt import BayesianOptimization
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
def rf_evaluate(n_estimators, max_depth, min_samples_split):
    rf = RandomForestClassifier(n_estimators=int(n_estimators),
                                max_depth=int(max_depth),
                                min_samples_split=int(min_samples_split),
                                random_state=42)
    scores = cross_val_score(rf, X_train, y_train, cv=5, scoring='f1')
    return scores.mean()

bounds = {
    'n_estimators': (50, 200),
    'max_depth': (5, 20),
    'min_samples_split': (2, 10),
}

f1_array = []
for i in range(100):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=i)

    optimizer = BayesianOptimization(
        f=rf_evaluate,
        pbounds=bounds,
        random_state=42,
    )

    optimizer.maximize(init_points=5, n_iter=25)

    best_params = optimizer.max['params']
    best_model = RandomForestClassifier(n_estimators=int(best_params['n_estimators']),
                                         max_depth=int(best_params['max_depth']),
                                         min_samples_split=int(best_params['min_samples_split']),
                                         random_state=42)

    best_model.fit(X_train, y_train)
    y_pred = best_model.predict(X_val)
    val_accuracy = f1_score(y_val, y_pred)
    print(val_accuracy)
    f1_array.append(val_accuracy)
