# Sleep classifier feature contract

This module curates the nine numeric inputs from the final college training variant. Training code should obtain its inputs with `training_features(frame)`, fit its scaler on training rows only, and build its output layer with `len(encoder.classes_)` units. Inference calls `predict(values, model, scaler, encoder)` so feature order, artifact dimensions and label ordering are validated together.

The old Flask app fabricated categorical defaults and produced 28 values. This adapter does not invent gender, occupation or BMI inputs. It rejects missing/nonfinite/negative numeric values, incompatible shapes, reordered/unnamed scalers and invalid probability outputs. Numeric checks are technical validation, not clinically established ranges.

Use `python -m unittest discover -s tests -v`. Tests use a real fitted scaler and a deterministic model stub; they do not validate TensorFlow inference or clinical accuracy. No legacy pickle or model was deserialized in this change. Legacy artifacts must be inspected and, if incompatible, regenerated together using this contract before a live app migration. The original notebook also has split-before-scaling and target-parsing work scheduled separately. This module is a tested contract foundation, not a deployed sleep prediction service.
