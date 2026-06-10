import pandas as pd
import os
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def train_and_save_model(data_path, models_dir):
    df = pd.read_csv(data_path)
    features = ['doomscroll_hrs', 'caffeine_mg', 'touch_grass_mins', 'deep_focus_hrs']
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2, random_state=42)
    pca.fit(X_scaled)

    model_artifacts = {
        'scaler': scaler,
        'pca': pca,
        'features': features
    }

    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, 'pca_inverse_artifacts.pkl'), 'wb') as f:
        pickle.dump(model_artifacts, f)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    train_and_save_model(os.path.join(base_dir, 'data', 'lifestyle_stats.csv'), os.path.join(base_dir, 'models'))