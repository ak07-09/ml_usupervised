import pandas as pd
import os
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

def train_and_save_model(data_path, models_dir):
    df = pd.read_csv(data_path)
    features = ['rizz', 'aura', 'lore', 'delusion']
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    gmm = GaussianMixture(n_components=3, covariance_type='full', random_state=42)
    gmm.fit(X_scaled)

    model_artifacts = {
        'scaler': scaler,
        'gmm': gmm,
        'features': features
    }

    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, 'gmm_artifacts.pkl'), 'wb') as f:
        pickle.dump(model_artifacts, f)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    train_and_save_model(os.path.join(base_dir, 'data', 'stats.csv'), os.path.join(base_dir, 'models'))