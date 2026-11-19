import numpy as np

def pairwise_cosine_similarity(X):
    X = np.asarray(X)
    # Normalize rows
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.maximum(norms, 1e-12) # Avoid division by zero
    X_normalized = X / norms
    # Dot product of normalized vectors gives cosine similarity matrix
    return X_normalized @ X_normalized.T