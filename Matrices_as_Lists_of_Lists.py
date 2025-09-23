# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
# Patrick Honner 9/21/22

# Need this to deepcopy lists
import copy

# Makes presenting a table of data easier
from tabulate import tabulate

# We'll hardcode the matrix as a list of lists
# The nested lists function as the rows of the matrix
def print_row(A, r):
  for i in range(len(A[r])):
    print(A[r][i], "\t", end="")
  print("\n")
def print_col(A, c):
  for i in range(len(A)):
    print(A[i][c])

def scalar_mult(A, row, scalar):
  for i in range(len(A[row])):
      A[row][i]=scalar*A[row][i]+0

def add_rows(A, added, addend, scalar):
  for i in range(len(A[added])):
    A[added][i]=A[added][i]+scalar*A[addend][i]+0

def interchange_rows(A, r1, r2):
  row_one = copy.copy(N[r1])
  N[r1]=N[r2]
  N[r2]=row_one

def rref(A):
  row_count = len(A)
  col_count = len(A[0])
  start_row = 0
  start_col = 0
  while (start_row<row_count and start_col<col_count):
    top_row = start_row
    has_top_row = False
    j = start_col
    i = start_row
    while (j in range(start_col, col_count) and not has_top_row):
      while (i in range(start_row, row_count) and not has_top_row):
        if (A[i][start_col] != 0):
          has_top_row = True
          interchange_rows(A, i, top_row)
        else:
          start_row += 1
          i += 1
      if not has_top_row:
        start_col += 1
        j += 1
    if has_top_row:
      scalar_mult(A, start_row, 1/float(A[start_row][start_col]))
    for i in range(row_count):
      if i != start_row:
        add_rows(A, i, start_row, -A[i][start_col])
    #for debugging purposes
    print("start_row = "+str(start_row))
    print("start_col = "+str(start_col))
    print(tabulate(A))
    start_row += 1
    start_col += 1



row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3]


print("Here is matrix M shown as a table in Python:\n")
print(tabulate(M))


# Create a new copy of the matrix
# deepcopy creates a copy of values, not a copy of references
N = copy.deepcopy(M)

# Ask user to perform an elementary row operation
end = False
while (not end):
  operation_choice = input("Choose an operation to do:\n [r] to return a given row \n [c] to return a given column \n [ch] to change an entry \n [s] to multiply a row by a scalar \n [a] to add a multiple of a row to another row \n [i] to interchange two rows \n [m] to enter a new matrix \n [rref] to put the matrix in reduced row echelon form \n [e] to exit \n")
  if operation_choice.lower() == "r":
    row_choice = input("Choose a row to display: ")
    row = int(row_choice) - 1
    print("Here is row "+row_choice+": ")
    print_row(N, row)
  elif operation_choice.lower() == "c":
    col_choice = input("Choose a column to display: ")
    col = int(col_choice) - 1
    print("Here is col "+col_choice+": ")
    print_col(N, col)
  elif operation_choice.lower() == "ch":
    row_choice = input("Input the row of the entry you are changing: ")
    col_choice = input("Input the column of the entry you are changing: ")
    new_val = input("Input the new value you would like to change the entry to: ")
    N[int(row_choice)-1][int(col_choice)-1]=new_val
    print("Here is your modified matrix: ")
    print(tabulate(N))
  elif operation_choice.lower() == "s":
    row_choice = input("Choose a row to multiply by a scalar:  ")
    scalar = input("Enter a scalar to multiply by:  ")
    scalar_mult(N, int(row_choice)-1, float(scalar))
    print("Here is the new matrix:")
    print(tabulate(N))
  elif operation_choice.lower() == "a":
    added_row = input("What row are you adding to? ")
    addend = input("You are adding a scalar multiple of which row to row "+added_row+"? ")
    scalar = input("What multiple of row "+addend+" are you adding to row "+added_row+"? ")
    add_rows(N, int(added_row)-1, int(addend)-1, float(scalar))
    print("Here is the new matrix:")
    print(tabulate(N))
  elif operation_choice.lower() == "i":
    user_rows = input("Input the two rows you are interchanging, separated by a space. ")
    swapped_rows = user_rows.split()
    interchange(A, int(swapped_rows[0])-1, int(swapped_rows[1])-1)
    print("Here is the new matrix:")
    print(tabulate(N))
  elif operation_choice.lower() == "m":
    row_count = int(input("How many rows would you like your matrix to have? "))
    col_count = int(input("How many columns would you like your matrix to have? "))
    N = [[0 for x in range(col_count)] for y in range(row_count)]
    for i in range(row_count):
      new_row = (input("Enter in row "+str(i+1)+" here, with values separated by spaces: ")).split()
      row_length = min(col_count, len(new_row))
      for j in range(row_length):
        N[i][j]=int(new_row[j])
    print("Here is the new matrix:")
    print(tabulate(N))
  elif operation_choice.lower() == "rref":
      rref(N)
      print("Here is the matrix in reduced row echelon form:")
      print(tabulate(N))
  elif operation_choice == "e":
    end = True
  else:
    print("Please enter a valid option.")





# A function to print out a list of lists, i.e. a matrix
# tabulate is nicer, so I didn't use this, but left as an example
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")
