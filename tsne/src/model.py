import pandas as pd
import os
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.neighbors import KNeighborsRegressor

def train_and_save_model(data_path, models_dir):
    df = pd.read_csv(data_path)
    features = ['thrift_energy', 'gorpcore_utility', 'y2k_nostalgia', 'avant_garde']
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    tsne = TSNE(n_components=2, perplexity=40, random_state=42)
    tsne_coords = tsne.fit_transform(X_scaled)

    inverse_bridge = KNeighborsRegressor(n_neighbors=5, weights='distance')
    inverse_bridge.fit(tsne_coords, X_scaled)

    model_artifacts = {
        'scaler': scaler,
        'inverse_bridge': inverse_bridge,
        'features': features
    }

    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, 'tsne_inverse_artifacts.pkl'), 'wb') as f:
        pickle.dump(model_artifacts, f)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    train_and_save_model(os.path.join(base_dir, 'data', 'drip_stats.csv'), os.path.join(base_dir, 'models'))