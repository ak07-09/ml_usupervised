import os
import joblib
import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def load_data():

    base_dir = os.path.dirname(
        os.path.dirname(__file__)
    )

    file_path = os.path.join(
        base_dir,
        "data",
        "creditcard.csv"
    )

    return pd.read_csv(file_path)


def preprocess_data(df):

    # Keep only numeric columns
    X = df.select_dtypes(
        include=["int64", "float64"]
    )

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled


def train_model(X):

    os.makedirs(
        "models",
        exist_ok=True
    )

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(X)

    joblib.dump(
        model,
        "models/isolation_forest.pkl"
    )


def load_model():

    return joblib.load(
        "models/isolation_forest.pkl"
    )