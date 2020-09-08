from smth.Game1 import Robot
from smth.Game2 import Human
def CompetitiveGame():
    CompetitiveWins = 0
    CompetitiveLoses = 0
    ScoreRobot = 0
    ScoreHuman = 0
    while ScoreRobot < 5 or ScoreHuman < 5:
        ScoreRobot += Robot()
        ScoreHuman += Human()
    if ScoreRobot > ScoreHuman:
        print("Robot wins")
        CompetitiveLoses += 1
    elif ScoreRobot < ScoreHuman:
        print("Human wins")
        CompetitiveWins += 1
    else:
        print("Tie")
    return ScoreRobot, ScoreHuman


