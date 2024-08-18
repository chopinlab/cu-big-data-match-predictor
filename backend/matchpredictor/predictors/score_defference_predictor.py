from typing import List
from matchpredictor.matchresults.result import Fixture, Outcome, Result
from matchpredictor.predictors.predictor import Predictor, Prediction


# (Added) This class predicts match outcomes based on the average score difference of teams.
class ScoreDifferencePredictor(Predictor):
    def __init__(self, past_results: List[Result]) -> None:
        self.team_score_diffs = self._calculate_team_score_diffs(past_results)

    def _calculate_team_score_diffs(self, results: List[Result]) -> dict:
        team_score_diffs = {}
        
        for result in results:
            home_team = result.fixture.home_team
            away_team = result.fixture.away_team

            home_diff = result.home_goals - result.away_goals
            away_diff = result.away_goals - result.home_goals

            if home_team.name not in team_score_diffs:
                team_score_diffs[home_team.name] = []
            if away_team.name not in team_score_diffs:
                team_score_diffs[away_team.name] = []

            team_score_diffs[home_team.name].append(home_diff)
            team_score_diffs[away_team.name].append(away_diff)

        # Calculate the average score difference for each team.
        return {team: sum(diffs) / len(diffs) for team, diffs in team_score_diffs.items()}

    def predict(self, fixture: Fixture) -> Prediction:
        home_team_diff = self.team_score_diffs.get(fixture.home_team.name, 0)
        away_team_diff = self.team_score_diffs.get(fixture.away_team.name, 0)

        if home_team_diff > away_team_diff:
            return Prediction(outcome=Outcome.HOME)
        elif away_team_diff > home_team_diff:
            return Prediction(outcome=Outcome.AWAY)
        else:
            return Prediction(outcome=Outcome.DRAW)
