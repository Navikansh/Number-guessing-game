
def input_limits():
     while True:
        try:
            #Ask for lower limit
            lower_limit = int(input('What\'s the lower limit ? ').strip())

            #Ask for upper limit
            upper_limit = int(input('What\'s the upper limit ? ').strip())
            if lower_limit > upper_limit:
                print('Upper limit is supposed to be greater than lower limit !!! \nTry again')
                continue
            elif upper_limit - lower_limit <= 3:
                print('Come on, atleast make it a bit challenging!! \nTry again')
                continue
            return lower_limit, upper_limit
        except ValueError:
            print('Please pass a valid input!!')
            pass


def input_guess(lives, num):
    chances = lives
    while lives > 0:
        try:
            #Ask for guess
            guess = int(input('Your Guess: ').strip())
            if guess == num:
                print('YAY you guessed it !!!')
                print(f'You took {int(chances - lives + 1)} chances')
                break
            elif guess > num:
                print('NOPE, your guess is too high!')
                lives -= 1
                print(f'{lives} lives left!')
            elif guess < num :
                print('NOPE, your guess is too low!!')
                lives -= 1
                print(f'{lives} lives left!')
        except ValueError:
            print('Please type a valid input!!')
            pass
    if lives == 0:
        print('GAME OVER')