class Grid:
    #This initializes the class and creates the grid. The grid is full of X's and we assign the middle pieces with W and B
    # X represents blank space
    def __init__(self):
        self.grid = [['X' for x in range(8)] for y in range(8)] 
        self.grid[3][3] = 'W'
        self.grid[3][4] = 'B'
        self.grid[4][3] = 'B'
        self.grid[4][4] = 'W'
    
    #This displays the current grid
    def printGrid(self):
        row = ''
        for x in range (len(self.grid)):
            for y in range(len(self.grid[0])):
                row += self.grid[x][y] + ' '
            print(row)
            row = ''
    #This is used to place the pieces on the grid. It checks to see if the coordinates passed in are valid
    def place(self,xCor,yCor,color):
        if xCor not in range(0,len(self.grid)) or yCor not in range(0,len(self.grid)) or isinstance(xCor,int) == False or isinstance(yCor,int) == False:
            print("This is not a valid coordinate")
            return False
        else:
            self.grid[xCor][yCor] = color
            self.printGrid()
            return True
        
    def flip(self,xCor,yCor):
        for i in range(-1,2):
            for j in range(-1,2):
                if self.grid[xCor + i][yCor + j] == 'W'
                

sup = Grid()
sup.printGrid()
lol = input("enter")
print (lol)
