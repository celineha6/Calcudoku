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
         
   
   # pzl_print = []
   # cell = 0
   # while cell < 25:
   #    pzl_print.append(puzzle[cell//5][cell%5])    #print the value of the pzl at the indices 
   #    cell += 1                                 #add 1 to cell

   # pzl_print = [str(n) for n in pzl_print]      #print the puzzle
   # print(" ")
   # print("--Solution--")
   # print(" ")
   # for val in range(5):
   #    print(" ".join(pzl_print[(val*5):((val+1)*5)])+" ") #joins the element in the list and prints them 

   # print("\nchecks:", check, "backtracks:", backtrack) #displays the number of checks and backtracks 

if __name__ == '__main__':
   main()
