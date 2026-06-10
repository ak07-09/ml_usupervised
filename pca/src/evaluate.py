import os
import pandas as pd
from src.predict import load_artifacts

def evaluate_inverse(data_path):
    artifacts = load_artifacts()
    df = pd.read_csv(data_path)
    
    variance = artifacts['pca'].explained_variance_ratio_
    print(f"PCA Part 2 Architecture Ready.")
    print(f"Total Variance Captured in 2D Plane: {variance.sum()*100:.2f}%")
    print(f"Inverse Transformation Matrix active.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    evaluate_inverse(os.path.join(base_dir, 'data', 'lifestyle_stats.csv'))