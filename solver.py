from solverFuncs import *

def main():

   cages = get_cages()
   puzzle = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
   backtrack = 0
   check = 0
   box = 0
   
   while box < 25:
      print(puzzle)
      puzzle[box//5][box%5] += 1
      # if puzzle[box//5][box%5] < 5:                #if the value of the square is less than 5
         # puzzle[box//5][box%5] += 1                #add 1 to the value of the square
      check += 1                                 #add 1 check
      if check_valid(puzzle, cages) == True:    #if the box is valid return true 
         box += 1                               #add 1 to the box 
      else:
         while puzzle[box//5][box%5] == 5:            #if the value of the box equals 5 set it to 0
            puzzle[box//5][box%5] = 0                 #
            backtrack += 1                         #add 1 to backtrack
            box -= 1                               #goes back to previous box

if __name__ == '__main__':
   main()
