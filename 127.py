import random
class GuessTheNumber:
    def getInput(self, playerNumber):
        return int(input(f"Player {playerNumber}: "))
    def check(self, guess):
        if guess<self.number:
            print("Enter a greater number!")
            return False
        elif guess == self.number: 
            return True
        elif guess>self.number:
            print("Enter a smaller number!")
            return False
    def __init__(self, nPlayer) -> None:
        self.currentplayer = 1
        Lguesses = {}
        a = int(input("Enter the lower Bound: "))
        b = int(input("Enter the upperbound: "))
        while self.currentplayer < nPlayer+1:
            self.number = random.randrange(a, b+1)
            self.nGuesses = 0
            self.isGuessed = False
            while not self.isGuessed:   
                guess = self.getInput(self.currentplayer)
                self.isGuessed = self.check(guess)
                self.nGuesses+=1
            if self.isGuessed:
                print(f"Player {self.currentplayer} Guessed the number in {self.nGuesses} guesses")
            try: 
                a = Lguesses[self.nGuesses]
                l = []
                l.append(a)
                l.append(f"Player {self.currentplayer}")
                Lguesses[self.nGuesses] = l
            except Exception as e:
                Lguesses.update({self.nGuesses : f"Player {self.currentplayer}"})
            self.currentplayer+=1
        m = max(Lguesses.keys())
        print(Lguesses[m], " wins!")

        
NumberOfPlayers = 2
GuessTheNumber(NumberOfPlayers)