import os
import joblib
import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


def load_data():

    data_path = os.path.join(
        BASE_DIR,
        "data",
        "creditcard.csv"
    )

    print("Dataset Path:", data_path)

    return pd.read_csv(data_path)


def preprocess_data(df):

    X = df.select_dtypes(
        include=["int64", "float64"]
    )

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled


def train_model(X):

    model_dir = os.path.join(
        BASE_DIR,
        "models"
    )

    os.makedirs(
        model_dir,
        exist_ok=True
    )

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(X)

    model_path = os.path.join(
        model_dir,
        "isolation_forest.pkl"
    )

    joblib.dump(
        model,
        model_path
    )

    print("Model Saved At:", model_path)


def load_model():

    model_path = os.path.join(
        BASE_DIR,
        "models",
        "isolation_forest.pkl"
    )

    print("Loading Model From:", model_path)

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model not found at {model_path}"
        )

    return joblib.load(model_path)