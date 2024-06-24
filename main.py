import user_input 
import numGenerator
import math

def main():
   #Take limits from user
   lowl, upl = user_input.input_limits()

   #Calculate lives
   lives = int(math.log(upl - lowl + 1, 2))
   print(f'You have {lives} chances')

   #Generate num between given limits
   user_input.input_guess(lives, numGenerator.num_generator(lowl, upl))
   
if __name__ == '__main__':
   main()