import pickle
import numpy as np
import os

def load_artifacts():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base_dir, 'models', 'pca_inverse_artifacts.pkl'), 'rb') as f:
        return pickle.load(f)

def run_inverse_inference(target_pc1, target_pc2):
    artifacts = load_artifacts()
    
    target_coords = np.array([[target_pc1, target_pc2]])
    scaled_reconstruction = artifacts['pca'].inverse_transform(target_coords)
    real_world_stats = artifacts['scaler'].inverse_transform(scaled_reconstruction)[0]
    real_world_stats = np.clip(real_world_stats, 0, None)
    
    return {
        'doomscroll_hrs': real_world_stats[0],
        'caffeine_mg': real_world_stats[1],
        'touch_grass_mins': real_world_stats[2],
        'deep_focus_hrs': real_world_stats[3]
    }