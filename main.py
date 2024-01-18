import random

class Die:

    def __init__(self):
        self._value = None 

    @property 
    def value(self):
        return self._value 
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value 
        return new_value

class Player:
    def __init__(self, die, is_computer=False):
        self._die = die 
        self._is_computer = is_computer
        self._counter = 10 

    @property 
    def die(self):
        return self._die 
    
    @property 
    def is_computer(self):
        return self._is_computer 
    
    @property 
    def counter(self):
        return self._counter 
    
    def increment_counter(self):
        self._counter += 1 

    def decrement_counter(self):
        self._counter -= 1 

    def roll_die(self):
        return self._die.roll() 
    

class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer 

    def play(self):
        print("===============================")
        print("Welcome to Roll the Dice!")
        print("===============================")
        while True:
            self.play_round() 
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome the user 
        self.print_round_welcome()

        # Roll the die
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die() 

        # show the value
        self.show_dice(player_value, computer_value)

        # Determin winner and looser
        if player_value > computer_value:
            print("You won the round!")
            self.update_counters(winner=self._player, looser=self._computer)
        elif computer_value > player_value:
            print("Computer won the round. Try again")
            self.update_counters(winner=self._computer, looser=self._player)
        else:
            print("It's a tie!!")

        # show counter
        self.show_counters()


    def print_round_welcome(self):
        print("\n--------- New round ---------")
        input("Press any key to roll the die 😰🙄")

    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"computer die: {computer_value}\n")

    def update_counters(self, winner, looser):
        winner.decrement_counter()
        looser.increment_counter()

    def show_counters(self):
        print(f"\nYour counter is : {self._player.counter}")
        print(f"Computer counter is: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter ==0:
            self.show_game_over(self._player)
            return True 
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True 
        else:
            return False
        
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n ====================== ")
            print(" G A M E    O V E R")
            print("The computer won the game. Sorry..")
            print("\n ====================== ")
        else:
            print("\n ====================== ")
            print(" G A M E    O V E R")
            print("You won the game. Congratulations..")
            print("\n ====================== ")  


player_die = Die() 
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

game.play()