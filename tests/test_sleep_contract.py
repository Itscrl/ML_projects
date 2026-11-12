import unittest
from types import SimpleNamespace
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sleep_classifier.contract import FEATURES, feature_row, training_features, predict, validate_artifacts

class Model:
    input_shape=(None,9)
    output_shape=(None,2)
    def predict(self, values, verbose=0): return np.array([[.25,.75]])

class SleepContract(unittest.TestCase):
    def setUp(self):
        self.values=dict(zip(FEATURES,range(1,10)))
        self.scaler=MinMaxScaler().fit(pd.DataFrame([range(9),range(1,10)],columns=FEATURES))
        self.encoder=SimpleNamespace(classes_=np.array(['Insomnia','Sleep Apnea']))
    def test_input_order_is_independent_of_form_order(self):
        np.testing.assert_array_equal(feature_row(dict(reversed(list(self.values.items())))),[range(1,10)])
    def test_training_uses_same_order(self):
        frame=pd.DataFrame([self.values]); self.assertEqual(tuple(training_features(frame).columns),FEATURES)
    def test_valid_prediction_uses_encoder_order(self):
        self.assertEqual(predict(self.values,Model(),self.scaler,self.encoder)['label'],'Sleep Apnea')
    def test_invalid_inputs_are_rejected(self):
        for value in [None,'bad',float('nan'),float('inf'),-1]:
            with self.subTest(value=value),self.assertRaises(ValueError): feature_row({**self.values,'Age':value})
        with self.assertRaises(ValueError): feature_row({})
    def test_mismatched_model_classes_are_rejected(self):
        model=Model();model.output_shape=(None,3)
        with self.assertRaises(ValueError):validate_artifacts(model,self.scaler,self.encoder)
    def test_reordered_scaler_is_rejected(self):
        self.scaler.feature_names_in_=np.array(list(reversed(FEATURES)))
        with self.assertRaises(ValueError):validate_artifacts(Model(),self.scaler,self.encoder)
    def test_old_feature_count_is_rejected(self):
        self.scaler.n_features_in_=28
        with self.assertRaises(ValueError):validate_artifacts(Model(),self.scaler,self.encoder)
