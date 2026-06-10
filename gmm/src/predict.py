import pickle
import pandas as pd
import os

def load_artifacts():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # THE FIX: Pointing to gmm_artifacts.pkl instead of tsne
    with open(os.path.join(base_dir, 'models', 'gmm_artifacts.pkl'), 'rb') as f:
        return pickle.load(f)

def run_inference(input_dict):
    artifacts = load_artifacts()
    df_input = pd.DataFrame([input_dict])[artifacts['features']]
    X_scaled = artifacts['scaler'].transform(df_input)
    
    probs = artifacts['gmm'].predict_proba(X_scaled)[0]
    cluster = artifacts['gmm'].predict(X_scaled)[0]
    
    return probs, cluster