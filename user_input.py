
def user_input():
     while True:
        try:
            #Ask for lower limit
            lower_limit = int(input('What\'s the lower limit ? ').strip())

            #Ask for upper limit
            upper_limit = int(input('What\'s the upper limit ? ').strip())
            break
        except ValueError:
            pass