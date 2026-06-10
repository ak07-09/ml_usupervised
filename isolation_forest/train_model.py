from src.anomaly_utils import (
    load_data,
    preprocess_data,
    train_model
)

df = load_data()

X = preprocess_data(df)

train_model(X)

print("Model trained and saved successfully!")