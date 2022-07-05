
import random
import math

def guess_the_number(min_num , max_num):
    bottom = min(min_num, max_num)
    top = max(min_num, max_num)
    random_num = random.randint(bottom , top )
    guess_num = 0
    while guess_num != random_num:
        try:
            guess_num = int(input(f'Guess a number between {bottom} and {top}\n'))
            if  guess_num < random_num:
                print('Try to guess again. It\'s too low.')
            elif guess_num > random_num:
                print('Try to guess again. It\'s too high.')
        except:
            pass
    print(f'Yes! You have guessed the number {random_num} correctly!')
    
def robot_guess_my_number(min_num , max_num):
    bottom = min(min_num, max_num)
    top = max(min_num, max_num)
    fback = ''
    while fback != 'c':
        if  top!=bottom:
            guess = random.randint(bottom, top)
        else:
            guess = bottom
        fback = input(f'Is {guess} too high(H), too low(L), or correct(C)?').lower()
        if fback == 'h':
            top = guess -1
        elif fback == 'l':
            bottom = guess + 1
    print(f"Got you! Robot won the human, and guess your mind number {guess}\n\
    .... Initialize the Skynet....\nOh, sorry it is my issues $@!vD ))")

def main():
    guess_the_number(1, 1000) # u play with robot
    robot_guess_my_number(1, 1000) # robot play with u
    input("Press the Enter to close this window...")

if __name__ == '__main__':
    main()