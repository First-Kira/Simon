import random
import time
import os

class SimonGame:
    COLORS = ["red", "green", "blue", "yellow"]

    def __init__(self):
        self.sequence = []
        self.player_sequence = []
        self.score = 0

    def play(self):
        print("Welcome to Simon Game!")
        while True:
            self.add_random_color()
            self.display_sequence()
            self.get_player_sequence()
            if not self.correct_sequence():
                break
            self.score += 1
            print(f"Correct! Your score is: {self.score}")
        self.game_over()

    def add_random_color(self):
        self.sequence.append(random.choice(self.COLORS))

    def display_sequence(self):
        print("Watch the sequence carefully!")
        for color in self.sequence:
            print(color)
            time.sleep(1)
            self.clear_screen()
            time.sleep(0.5)

    def get_player_sequence(self):
        self.player_sequence.clear()
        print("Now it's your turn to repeat the sequence.")
        for i in range(len(self.sequence)):
            color = input(f"Enter color #{i + 1}: ").strip().lower()
            self.player_sequence.append(color)

    def correct_sequence(self):
        return self.sequence == self.player_sequence

    def game_over(self):
        print(f"Game Over! Your final score is: {self.score}")

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    game = SimonGame()
    game.play()

