'''
Following is a recreation of Fallout Hacking Game found in Fallout3
https://www.reddit.com/r/dailyprogrammer/comments/3qjnil/20151028_challenge_238_intermediate_fallout/
Done with OOP
'''

#enable1.txt is a text file dictionary

with open('enable1.txt','r') as f:
    lines = f.read().split()

import random

class WordCreate:
    
    def __init__(self,diff):
        self.words = []
        self.diff = diff
        self.build()
        
    def build(self):
        self.words = [x for x in lines if len(x) == self.diff]
        self.words = random.sample(self.words,8)
        print(self.words)
        return self.words   


class GuessGame(WordCreate):
    
    def __init__(self,diff):
        self.guess=[]
        super().__init__(diff)
        self.pickem = random.sample(self.words,1)
        self.answer = ''
        for x in self.pickem:
            self.answer = x
        
    def guess_check(self):
        while len(self.guess) < 5:
            guess = input()
            self.guess.append(guess)
            
            if guess == str(self.answer):
                print('Correct, you win')
                break
            else:
                count = 0
                for x in range(len(self.answer)):
                    if self.answer[x] == guess[x]:
                        count+=1
                print(f"{count} of the letter positions are correct")
        else:
            print('Game over, you lose')
        
    def printing(self):
        print(self.words)
        print(self.answer)
    