class Grid:
    def __init__(self):
        self.grid = [['X' for x in range(8)] for y in range(8)] 
        self.grid[3][3] = 'W'
        self.grid[3][4] = 'B'
        self.grid[4][3] = 'B'
        self.grid[4][4] = 'W'
        
    def printGrid(self):
        row = ''
        for x in range (len(self.grid)):
            for y in range(len(self.grid[0])):
                row += self.grid[x][y] + ' '
            print(row)
            row = ''
    def place(self,xCor,yCor,color):
        if xCor >= len(self.grid[0]) or yCor >= len(self.grid) or xCor < 0 or yCor < 0:
            print("This is not a valid coordinate")
        self.grid[xCor][yCor] = color
        self.printGrid()

sup = Grid()
sup.printGrid()