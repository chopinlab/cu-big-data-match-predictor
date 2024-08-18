from unittest import TestCase
from matchpredictor.matchresults.results_provider import validation_results
from matchpredictor.evaluation.evaluator import Evaluator
from matchpredictor.predictors.score_defference_predictor import ScoreDifferencePredictor

from test.predictors import csv_location

class TestScoreDifferencePredictor(TestCase):
    def test_accuracy(self) -> None:
        validation_data = validation_results(csv_location, 2019)
        model = ScoreDifferencePredictor(validation_data)
        accuracy, _ = Evaluator(model).measure_accuracy(validation_data)

        self.assertGreaterEqual(accuracy, 0.50)
