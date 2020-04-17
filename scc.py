import random

players = {}     # stores players as player num : Player

class Die():
    # Creates the top face of a randomly rolled die
    def __init__(self):
        self.value = random.randint(1, 6)

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.value)
    


class Hand():
    # Creates a hand of five Die instances
    def __init__(self):
        self.dice = []
        self.ship = False
        self.captain = False
        self.crew = False
        self.diceToRoll = 5
        self.rollsLeft = 3

    def roll(self):
        ''' Rolls dice remaining depending on whether a 6, 5, or 4 have already
            been rolled'''
        if self.rollsLeft > 0:
            self.dice = []
            for i in range(self.diceToRoll):
                die = Die()
                print(die)
                self.dice.append(die)
            self.rollsLeft -= 1
        else: print('Out of rolls')
        
    def get_value(self):
        # Checks if there is valid cargo and returns relevant score
        self.value = 0
        if self.ship and self.captain and self.crew:
            for die in self.dice:
                self.value += die.get_value()
        return self.value

    def check_for_scc(self):
        # Checks rolled dice for a 6, 5, or 4
        if not self.ship:
            for die in self.dice:
                if die.get_value() == 6:
                    self.ship = True
                    self.diceToRoll -= 1
                    self.dice.remove(die)
                    break
        if self.ship and not self.captain:
            for die in self.dice:
                if die.get_value() == 5:
                    self.captain = True
                    self.diceToRoll -= 1
                    self.dice.remove(die)
                    break
        if self.ship and self.captain and not self.crew:
            for die in self.dice:
                if die.get_value() == 4:
                    self.crew = True
                    self.diceToRoll -= 1
                    self.dice.remove(die)
                    break

    def __str__(self):
        show_dice = []
        for die in self.dice:
            show_dice.append(str(die.get_value()))
        return ' '.join(show_dice)

            
class Score():
    pass


class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name + ' ' + str(self.score)

def get_players():
    ''' Determines the number of players, gets their names, and stores data
        in a dictionary'''
    playerName = {}
    numPlayers = input('How many players? ')
    for player in range(int(numPlayers)):
        playerNum = 'Player ' + str(player +1)
        print(playerNum + ', what is your name?')
        name = input()
        playerName[player] = name.title()
    for num, name in playerName.items():
        players[num + 1] = Player(name, 0)

# TODO: Each player takes a turn
'''Check if player is still active in overall game
   roll 5 dice
   check for SCC
   output SCC and leftover dice values
   if SCC, and rolls left, ask if want to roll again
   wait for input to roll for more SCC
   once turn is over, input hand value into temp score for each player'''

# TODO: Compare temp scores for all players and determine winner
'''Add value to Player for hand score'''

# TODO: Loser takes a drink. Main score decreases by one
'''Output player tallies'''

# TODO: If a player has no drinks left, they are out
'''Add value to Player to determine if they are still active'''

# TODO: When only one player has a drink left, they win and game is over
                 
player1 = Hand()
player1.roll()
player1.check_for_scc()
print(player1.ship)
print(player1.captain)
print(player1.crew)
print('Value:', str(player1.get_value()))
player1.roll()
player1.check_for_scc()
print(player1.ship)
print(player1.captain)
print(player1.crew)
print('Value:', str(player1.get_value()))
player1.roll()
player1.check_for_scc()
print(player1.ship)
print(player1.captain)
print(player1.crew)
print('Value:', str(player1.get_value()))
player1.roll()
print(player1)
get_players()
players[1].score = 3
for i, j in players.items():
        print(i, j)


