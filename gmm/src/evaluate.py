import os
import pandas as pd
from src.predict import load_artifacts

def evaluate_gmm(data_path):
    artifacts = load_artifacts()
    df = pd.read_csv(data_path)
    print(f"GMM Trained on {len(df)} records.")
    print(f"Converged: {artifacts['gmm'].converged_}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    evaluate_gmm(os.path.join(base_dir, 'data', 'stats.csv'))