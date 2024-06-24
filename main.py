import user_input 
import numGenerator
import math

def main():
   #Take limits from user
   lowl, upl = user_input.input_limits()

   #Calculate lives
   lives = math.log(upl - lowl + 1, 2)

   #Generate num between given limits
   user_input.input_guess(lives, numGenerator.num_generator(lowl, upl))
   
if __name__ == '__main__':
   main()