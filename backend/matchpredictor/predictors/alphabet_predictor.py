from matchpredictor.matchresults.result import Fixture, Outcome
from matchpredictor.predictors.predictor import Prediction, Predictor


# (Added) This class predicts the outcome of a match based on the alphabetical order of team names.
class AlphabetPredictor(Predictor):
    def predict(self, fixture: Fixture) -> Prediction:
        home_team_name = fixture.home_team.name
        away_team_name = fixture.away_team.name

        if home_team_name < away_team_name:
            return Prediction(outcome=Outcome.HOME)
        elif home_team_name > away_team_name:
            return Prediction(outcome=Outcome.AWAY)
        else:
            return Prediction(outcome=Outcome.DRAW)