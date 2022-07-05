import random
import sys

def play_the_game():
    user_input = input("Pick one: (r)Rock or (p)Paper or (s)Scissors\n")
    robot_input = random.choice(['r', 'p', 's'])

    if user_input == robot_input:
        return 'It\'s a tie'
    elif is_winner(user_input, robot_input):
        return 'You won!'
    return 'You lost!'

def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') :
        return True

def main():
    print(play_the_game())


if __name__ == "__main__":
    main()