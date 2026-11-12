"""Nine-feature contract from the final undergraduate sleep training variant."""
import math
import numpy as np

FEATURES = ("Age", "Sleep Duration", "Quality of Sleep", "Physical Activity Level", "Stress Level", "Heart Rate", "Daily Steps", "Systolic_BP", "Diastolic_BP")

def feature_row(values):
    row = []
    for feature in FEATURES:
        try: value = float(values[feature])
        except (KeyError, TypeError, ValueError): raise ValueError(f"Missing or nonnumeric input: {feature}") from None
        if not math.isfinite(value) or value < 0: raise ValueError(f"Invalid input: {feature}")
        row.append(value)
    return np.asarray([row], dtype=float)

def training_features(frame):
    return frame.loc[:, list(FEATURES)]

def validate_artifacts(model, scaler, encoder):
    if getattr(scaler, "n_features_in_", None) != len(FEATURES): raise ValueError("Scaler must accept exactly nine features")
    names = getattr(scaler, "feature_names_in_", None)
    if names is None or tuple(names) != FEATURES: raise ValueError("Scaler must record the exact training feature order; regenerate artifacts if missing")
    if tuple(model.input_shape)[-1] != len(FEATURES): raise ValueError("Model input shape does not match the nine-feature contract")
    labels = tuple(str(x) for x in encoder.classes_)
    if not labels or len(set(labels)) != len(labels): raise ValueError("Invalid class labels")
    if tuple(model.output_shape)[-1] != len(labels): raise ValueError("Model output count and encoder labels disagree")
    return labels

def predict(values, model, scaler, encoder):
    labels = validate_artifacts(model, scaler, encoder)
    row = feature_row(values)
    # Retain named columns for scalers fitted on a training DataFrame.
    import pandas as pd
    scaled = scaler.transform(pd.DataFrame(row, columns=FEATURES))
    probabilities = np.asarray(model.predict(scaled, verbose=0), dtype=float)
    if probabilities.shape != (1, len(labels)) or not np.isfinite(probabilities).all(): raise ValueError("Invalid model output")
    if (probabilities < 0).any() or (probabilities > 1).any() or not np.isclose(probabilities.sum(), 1, atol=1e-5): raise ValueError("Expected normalized class probabilities")
    return {"label": labels[int(probabilities[0].argmax())], "probabilities": dict(zip(labels, probabilities[0].tolist()))}
