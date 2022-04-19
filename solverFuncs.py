# These are the required functions for this project.
#
# I highly recommend adding functions to check a single
# row, check a single column, and check a single cage.

def check_rows_valid(puzzle):
   row = 0
   while row < len(puzzle):
      if check_one_row(puzzle[row]) == False:
         return False
      row += 1
   return True 
      
       
# def check_columns_valid(puzzle):
#    column = 0
#    while column < len(puzzle):
#       if check_one_column(puzzle) == False:
#          return False
#       column += 1 
#    return True 

def check_cages_valid(puzzle, cages):
   loop = 0
   while loop < len(cages):
      if check_one_cage(puzzle,cages[loop]) == False:
         return False
      loop += 1 
   return True
      
       
def check_valid(puzzle, cages):
   if check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(puzzle, cages) == True:
      return True
   return False

def get_cages():
   loop = int(input('Number of Cages: '))
   count = 0
   new_list = []
   while count < loop:
      cage = input('Cage Number '+ str(count) +': ' )
      cage = cage.split()
      cage = [int(num) for num in cage]
      new_list.append(cage)
      count += 1
   return new_list

def check_columns_valid(puzzle):
   nlist = []
   for i in range(len(puzzle)):
      for c in range(len(puzzle[i])):
         nlist.append(puzzle[c][i])
      if check_one_row(nlist) == False:
         return False
      nlist = []
   return True 

def check_one_row(row):
   nums = [1,2,3,4,5]
   for num in nums:
      if row.count(num) > 1:
         return False 
   return True

   # for i in range(len(row)):
      # if row[i] == 0:
      #    return False
      # for c in range(len(row)-i-1):
      #    if row[c + i+1] == row[i]:
      #       return False

def check_one_cage(puzzle, cage):
   total_of_cage = cage[0]             #the first index number in the cage list is equal to the total of the cage
   total = 0                           #the total sum of everything in the cage is zero 
   zeros = False                       #the values of the squares are not zero 
   item = 0                            #the squares 

   for i in range(2, len(cage)):       #discludes the first two indices 
      item = cage[i]                   #item is equal to the value of cage[i]
      row = item // 5                  #the columns and rows that are in the puzzle
      col = item % 5                   
      total += puzzle[row][col]        #the total sum of everything in the cage is added with the value of the puzzle at that specified row and column 
      if puzzle[row][col] == 0:        #if the value of the puzzle is 0 
         zeros = True
  
   if total == total_of_cage and zeros == False:   #if the total of the squares equals the total of the cage and zeros is false 
      return True                                  
   elif zeros == True and total < total_of_cage:   #if the puzzle has zeros and the total is less than the total of the cage then the cage is still valid 
      return True
   return False                                     #cage is false if otherwise 



