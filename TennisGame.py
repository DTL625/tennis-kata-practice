class GameOne:

    def __init__(self, p1Score, p2Score):
        self.p1Pts = p1Score
        self.p2Pts = p2Score

        pass

    def getScoreResult(self):

        haveLovePt = (self.p1Pts == 0 or self.p2Pts == 0);
        isTie = (self.p1Pts == self.p2Pts);
        haveAdvString = self.getAdvString();
        haveWinnerString = self.getWinnerString();

        # 1. 含love
        if (haveLovePt and haveWinnerString == '' ):
            if (isTie):
                return 'Love-All';
            else:
                p1Str = self.getScoreString(self.p1Pts)
                p2Str = self.getScoreString(self.p2Pts)

                return p1Str + '-' + p2Str

        # 2. 平手（tie & deuce）
        elif (isTie):
            if (self.p1Pts < 3):
                return self.getScoreString(self.p1Pts) + '-All'
            else:
                return 'Deuce';
        # 3. 其中一名玩家獲得聽牌機會（adv）
        elif (haveAdvString):
            return haveAdvString
        # 4. 其中一名玩家獲勝
        elif (haveWinnerString):
            return haveWinnerString
        # 5. 其他
        else:
            p1Str = self.getScoreString(self.p1Pts)
            p2Str = self.getScoreString(self.p2Pts)

            return p1Str + '-' + p2Str

    # 將分數轉換成對應英文字串
    def getScoreString(self, pts):
        return {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty',
        }.get(pts, 'err')

    # 判斷是否有選手符合adv資格
    def getAdvString(self):
        minus = abs(self.p1Pts - self.p2Pts)
        if (self.p1Pts >= 3 and self.p2Pts >= 3 and minus == 1):
            player = 'Player1' if (self.p1Pts > self.p2Pts) else 'Player2'

            return player + ' get Advantage'
        else:
            return '';

    # 判斷是否有選手符合獲勝資格
    def getWinnerString(self):
        minus = abs(self.p1Pts - self.p2Pts)
        if (self.p1Pts >= 4 or self.p2Pts >= 4 and minus >= 2):
            player = 'Player1' if (self.p1Pts > self.p2Pts) else 'Player2'

            return 'Win for ' + player
        else:
            return '';