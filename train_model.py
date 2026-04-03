import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# load data
data = load_iris()
X, y = data.data, data.target

# train
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# save artifact
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model artifact saved as model.pkl")