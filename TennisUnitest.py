import unittest
from TennisGame import GameOne

# 測試用例，一共分為四類：
# 1. 含love
# 2. 平手（tie & deuce）
# 3. 其中一名玩家獲得聽牌機會（adv）
# 4. 其中一名玩家獲勝

testCases = [
    # # love
    (0, 0, "Love-All"), # (p1Score, p2Score, resultFromUnitest)
    (0, 1, "Love-Fifteen"),
    (0, 2, "Love-Thirty"),
    (0, 3, "Love-Forty"),
    (1, 0, "Fifteen-Love"),
    (2, 0, "Thirty-Love"),
    (3, 0, "Forty-Love"),

    # tie
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
    # Deuce
    (3, 3, "Deuce"),
    (4, 4, "Deuce"),
    (10, 10, "Deuce"),

    # others
    (1, 2, "Fifteen-Thirty"),
    (1, 3, "Fifteen-Forty"),
    (2, 1, "Thirty-Fifteen"),
    (2, 3, "Thirty-Forty"),
    (3, 1, "Forty-Fifteen"),
    (3, 2, "Forty-Thirty"),

    # Player get Advantage
    (4, 3, "Player1 get Advantage"),
    (3, 4, "Player2 get Advantage"),
    (5, 4, "Player1 get Advantage"),
    (4, 5, "Player2 get Advantage"),
    (11, 10, "Player1 get Advantage"),
    (10, 11, "Player2 get Advantage"),

    # win for Player
    (4, 0, "Win for Player1"),
    (0, 4, "Win for Player2"),
    (4, 1, "Win for Player1"),
    (1, 4, "Win for Player2"),
    (4, 2, "Win for Player1"),
    (2, 4, "Win for Player2"),
    (5, 3, "Win for Player1"),
    (3, 5, "Win for Player2"),
    (6, 4, "Win for Player1"),
    (4, 6, "Win for Player2"),
    (12, 10, "Win for Player1"),
    (10, 12, "Win for Player2"),
]

class TennisTest(unittest.TestCase):

    def testTennisGameOne(self):

        for testCase in testCases:
            # get result from test_case
            (p1Score, p2Score, resultFromUnitest) = testCase

            # get result from test_func
            game = GameOne(p1Score, p2Score)
            resultFromFunc = game.getScoreResult()

            # compaer result
            # if (resultFromUnitest == resultFromFunc):
            #     print('getSuccess-', end='')
            #     print('score(p1/p2):{}/{} result(test/func): {}/{}'.format(p1Score, p2Score, resultFromUnitest,
            #                                                                resultFromFunc))
            # else:
            #     print('getErr-', end='')
            #     print('score(p1/p2):{}/{} result(test/func): {}/{}'.format(p1Score, p2Score, resultFromUnitest,
            #                                                                resultFromFunc))
            #     pass

            self.assertEqual(resultFromUnitest, resultFromFunc)

if __name__ == '__main__':
    unittest.main()
