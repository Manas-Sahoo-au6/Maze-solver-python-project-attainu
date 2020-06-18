# ***********************************************************************************#
# date:-9/06/2020 :PYTHONE PROJECT
# (MAZE SOLVER USING BACK-TRACKING) by MANAS:      #
# ***********************************************************************************#
import argparse  # importing the command line python package
import datetime  # importing the datetime package use in the time of execution

# ******************************************************************/
#    THIS FUNCTION SOLVES THE MAZE PROBLEM USING BACKTRACKING. IT  #
#    RETURNS FALSE IF NO PATH IS AVAILABLE,OTHERWISE RETURNS TRUE. #
# ******************************************************************/


# conditional boundation and limits of maze solver problem checker Function
def maze_runner(row, col):
    # condition checking whether the destination element is 0 or not
    if maze[LENGTH-1][LENGTH-1] == 0:
        return False
    # if the final destination reached then
    if (row == LENGTH-1) and (col == LENGTH-1):
        solution[row][col] = 1
        return True
    if (row >= 0 and col >= 0 and row < LENGTH and col < LENGTH and
            solution[row][col] == 0 and maze[row][col] == 1):
        solution[row][col] = 1  # visiting the cell
        if maze_runner(row+1, col):  # going down
            return True
        if maze_runner(row-1, col):  # going up
            return True
        if maze_runner(row, col+1):  # going right
            return True
        if maze_runner(row, col-1):  # going left
            return True
        solution[row][col] = 0  # backtracking
        return False
    return False

# *******************************************************************************************************************

# *********************************************************************************#
#               FUNCTION TO PRINT THE THE PATH IN THE STRING FORAMTE     #
# *************************************************************************#


def print_function(sol):
    file2.write("***\n\n" + "the  path followed is " +
                printDirec(sol) + "reach to the destination: \n\n")
    for i in sol:
        for j in i:
            file2.write(" " + str(j) + " ")
        file2.write('\n')
        # print the output path in matrix form

    time = datetime.datetime.now()
    # call the date time inbuild function that generate the local date time

    file2.write("***\n" + "Time of execution at : " +
                time.strftime("%d-%m-%Y * %H:%M:%S\n" + "***\n\n"))
    # printing the the path by notaion up down left right notaion


# ******************************************************************************#
#  FUNCTION THAT CHECK THE MOVMENT OF CELL
# TO REACH THE MAZE TO IT'S DESTINATION
#                 notice-:This is the extra feature
# ************************************************************#

def printDirec(solvedMaze):  # call of direction printing function
    n = len(solvedMaze)    # finding the  lenghth of the solved maze
    # make a variable to store in a array cell intial as false
    visited = [[False for _ in range(n)] for _ in range(n)]
    # take blank string variable that store the the direction of movement
    arr = ""
    i = j = 0
    while i != n-1 or j != n-1:
        if j == n-1:
            if solvedMaze[i+1][j] == 1 and visited[i+1][j] is False:
                visited[i+1][j] = True
                i = i+1
                arr += "Down=>"
            elif solvedMaze[i][j-1] == 1 and visited[i][j-1] is False:
                visited[i][j-1] = True
                j = j-1
                arr += "Left=>"
        elif i == n-1:
            if solvedMaze[i][j+1] == 1 and visited[i][j+1] is False:
                visited[i][j+1] = True
                j = j+1
                arr += "Right=>"
            elif solvedMaze[i-1][j] == 1 and visited[i-1][j] is False:
                visited[i-1][j] = True
                i = i-1
                arr += "Up=>"
        else:
            if solvedMaze[i+1][j] == 1 and visited[i+1][j] is False:
                visited[i+1][j] = True
                i = i+1
                arr += "Down=>"
            elif solvedMaze[i][j+1] == 1 and visited[i][j+1] is False:
                visited[i][j+1] = True
                j = j+1
                arr += "Right=>"
            elif solvedMaze[i-1][j] == 1 and visited[i-1][j] is False:
                visited[i-1][j] = True
                i = i-1
                arr += "Up=>"
            elif solvedMaze[i][j-1] == 1 and visited[i][j-1] is False:
                visited[i][j-1] = True
                j = j-1
                arr += "Left=>"
    return arr


# *******************************************************************************#
#                          DRIVER FUNCTION                   #
# *******************************************************************************#


if __name__ == "__main__":
    maze = []   # appending all cell elemt from the comand line input by user
# TAKING FILE ARGUMENTS FROM COMMAND LINE.  (STEP-1)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input File")
    parser.add_argument("-o", help="Output File")
    args = parser.parse_args()
    file = open(args.i, 'r')  # input file
    file2 = open(args.o, 'a')  # output file

    # GENERATING MAZE FROM INPUTS (STEP-2)
    for data in file:
        [test.strip('\n\r') for test in data]
        maze.append([int(x) for x in data.split()])
    LENGTH = len(maze)
    # making a solution matrix and set all cell elemnt to zero initial
    solution = [[0]*LENGTH for _ in range(LENGTH)]

    # MAZE-RUNNER
    if(maze_runner(0, 0)):  # (STEP-3)
        print_function(solution)
    else:
        file2.write("***\n-1\n")
        file2.write(
            " sorry there is no any path available to reach destination.")
        now = datetime.datetime.now()
        file2.write("\nTime of execution at : " +
                    now.strftime("%d-%m-%Y * %H:%M:%S") + "\n***\n\n\n")
