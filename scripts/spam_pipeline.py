"""Shared training pipeline used by the spam notebook and regression tests."""
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def build_spam_pipeline():
    return make_pipeline(StandardScaler(), LogisticRegression(solver="liblinear", max_iter=1000, random_state=42))
