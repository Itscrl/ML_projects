import unittest
import numpy as np
from scripts.spam_pipeline import build_spam_pipeline

class TrainingOnlyScaling(unittest.TestCase):
    def test_held_out_extremes_do_not_change_training_statistics(self):
        train = np.array([[0., 1.], [1., 2.], [2., 3.], [3., 4.]])
        model = build_spam_pipeline()
        model.fit(train, [0, 0, 1, 1])
        scaler = model.named_steps["standardscaler"]
        expected = train.mean(axis=0)
        np.testing.assert_allclose(scaler.mean_, expected)
        model.predict(np.array([[1000000., -1000000.]]))
        np.testing.assert_allclose(scaler.mean_, expected)
        self.assertEqual(scaler.n_samples_seen_, len(train))

if __name__ == "__main__": unittest.main()
