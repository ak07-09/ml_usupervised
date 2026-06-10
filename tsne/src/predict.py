import pickle
import numpy as np
import os

def load_artifacts():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base_dir, 'models', 'tsne_inverse_artifacts.pkl'), 'rb') as f:
        return pickle.load(f)

def run_inverse_inference(tsne_x, tsne_y):
    artifacts = load_artifacts()
    
    target_coords = np.array([[tsne_x, tsne_y]])
    scaled_reconstruction = artifacts['inverse_bridge'].predict(target_coords)
    real_world_stats = artifacts['scaler'].inverse_transform(scaled_reconstruction)[0]
    real_world_stats = np.clip(real_world_stats, 0, 100)
    
    return {
        'thrift_energy': real_world_stats[0],
        'gorpcore_utility': real_world_stats[1],
        'y2k_nostalgia': real_world_stats[2],
        'avant_garde': real_world_stats[3]
    }